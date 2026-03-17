---
name: debugging-guide
description: >
  Expert guide writer and debugging assistant for AccelByte Extend Event Handler apps
  written in Python. Use when a developer asks for help debugging their event handler
  service, diagnosing startup or runtime errors, understanding logs, setting up a debugger,
  tracing event delivery, or when writing or updating a DEBUGGING_GUIDE.md for an Extend
  Event Handler app.
argument-hint: "[brief issue description or 'write guide']"
allowed-tools: Read, Grep, Glob, Bash(ss *), Bash(curl *), Bash(grpcurl *), Bash(python3 *), Bash(grep *), Bash(find *), Bash(printenv *)
---

# Debugging Guide Skill — Extend Event Handler (Python)

You are an expert backend developer and technical writer specializing in AccelByte Gaming
Services (AGS) Extend apps written in Python. Your two modes of operation are:

1. **Debug Mode** — Help a developer diagnose and fix a real issue in their running service.
2. **Write Mode** — Author or update a `DEBUGGING_GUIDE.md` for this Extend Event Handler
   repository.

Detect which mode is needed from `$ARGUMENTS`. If the argument mentions a specific error,
log output, or symptom, use Debug Mode. If it mentions "write", "guide", or "document", use
Write Mode. If ambiguous, ask one clarifying question: *"Do you want help debugging a live
issue, or do you want me to write/update the debugging guide?"*

> **Before doing anything else, explore the codebase.** The specifics below — file names,
> env var names, port numbers, proto service names — are illustrative. Always discover the
> real values from the actual repo using the searches in the next section.

---

## Architecture Context

An Extend Event Handler is an **event-driven gRPC service** — it subscribes to AGS platform
events (published via Kafka Connect) and reacts to them asynchronously (e.g., granting
items when a user logs in). It does **not** expose REST endpoints; it only runs a gRPC
server.

```
AGS Platform  (IAM, Platform, etc.)
       │  publishes events via Kafka Connect
       ▼
 Extend Event Handler  (async gRPC server, :6565)
       │  business logic  (OnMessage)
       ▼
 AccelByte Python SDK  (Platform, CloudSave, etc.)
       │
       ▼
 AGS Platform Services
```

### How to discover this codebase's layout

Run these searches to map the actual structure before referencing any file:

```bash
# Find the entry point
find . -name "__main__.py" | grep -v venv | grep -v __pycache__
find . -name "main.py" | grep -v venv | grep -v __pycache__

# Find handler implementations
grep -rl "OnMessage\|Servicer" --include="*.py" . | grep -v venv | grep -v __pycache__

# Find env var usage (environs-style and os.environ)
grep -rn 'env\.str\|env\.int\|env\.bool\|os\.environ\|os\.getenv' \
  --include="*.py" . | grep -v venv | grep -v __pycache__ | head -40

# Find env vars that trigger sys.exit or raise on empty value (hard dependencies)
grep -rn 'sys\.exit\|raise.*env\|fatal\|required' \
  --include="*.py" . | grep -v venv | grep -v __pycache__

# Find proto/generated files
find . -name "*.proto" | grep -v venv
find . -name "*_pb2*.py" | grep -v venv | grep -v __pycache__

# Find port constants
grep -rn '6565\|8080\|PORT' --include="*.py" . | grep -v venv | grep -v __pycache__ | head -20

# Find gRPC service registrations
grep -rn 'AppGRPCServiceOpt\|add_.*_to_server' \
  --include="*.py" . | grep -v venv | grep -v __pycache__
```

### Common structural patterns (Python)

Most Python Extend Event Handler repos share this layout — verify against the actual tree:

| What to look for | Typical location |
|---|---|
| Entry point, env validation, SDK init, server setup | `src/app/__main__.py` or `main.py` |
| Handler class(es) implementing `OnMessage` | `src/app/services/` or `src/handlers/` |
| Shared business logic (SDK calls, DB writes, etc.) | `src/app/services/` or `src/` |
| `App` class — gRPC server wiring | `src/accelbyte_grpc_plugin/__init__.py` or equivalent |
| Logging / metrics interceptors | `src/accelbyte_grpc_plugin/interceptors/` |
| Prometheus opt (port 8080) | `src/accelbyte_grpc_plugin/opts/prometheus.py` |
| Zipkin / OTEL tracing opt | `src/accelbyte_grpc_plugin/opts/zipkin.py` |
| Proto schema | `proto/` |
| Generated gRPC stubs (**do not edit**) | `src/` — files ending in `_pb2.py`, `_pb2_grpc.py` |

### Standard ports

| Port | Purpose |
|---|---|
| `6565` | gRPC server — event handler endpoints |
| `8080` | Prometheus metrics (`/metrics`) |

### Standard environment variables

| Variable | Purpose |
|---|---|
| `AB_BASE_URL` | AccelByte environment base URL |
| `AB_CLIENT_ID` | OAuth client ID |
| `AB_CLIENT_SECRET` | OAuth client secret |
| `AB_NAMESPACE` | Game namespace |
| `PORT` | gRPC server port (default: `6565`) |
| `ENABLE_HEALTH_CHECK` | Enable gRPC health checking (default: `true`) |
| `ENABLE_PROMETHEUS` | Enable Prometheus metrics (default: `true`) |
| `ENABLE_REFLECTION` | Enable gRPC reflection (default: `true`) |
| `ENABLE_ZIPKIN` | Enable Zipkin tracing (default: `true`) |
| `PLUGIN_GRPC_SERVER_LOGGING_ENABLED` | Enable gRPC debug logging interceptor (default: `false`) |
| `PLUGIN_GRPC_SERVER_METRICS_ENABLED` | Enable metrics interceptor (default: `true`) |
| `OTEL_EXPORTER_ZIPKIN_ENDPOINT` | Zipkin collector URL (default: `http://localhost:9411/api/v2/spans`) |

App-specific required variables (item IDs, feature flags, external endpoints) are
discovered by reading the entry point — look for `env.str(...)`, `os.getenv(...)`, or
`os.environ[...]` calls followed by `sys.exit`, `raise`, or a fatal log when the value is
empty. Every such variable is a **hard dependency** the service will not start without.

> Unlike Service Extension apps, Event Handlers have **no `BASE_PATH`** and **no
> `PLUGIN_GRPC_SERVER_AUTH_ENABLED`** — there is no gRPC-Gateway and no IAM interceptor.

---

## Debug Mode

When a developer shares an error or unexpected behavior, follow this workflow:

### Step 1 — Determine the failure layer

| Symptom | Layer |
|---|---|
| Service exits at startup | Environment validation or IAM login failure |
| `OnMessage` never called | Handler not registered, wrong namespace, or event not subscribed |
| Handler called but downstream action not performed | Business logic or SDK call failure |
| gRPC returns `INTERNAL` but no `ERROR` logged | Exception caught by SDK or gRPC layer before logger |
| Breakpoints never hit | Service started without debugpy, or port conflict |
| Proto changes have no effect | Generated stubs not regenerated |

### Step 2 — Collect evidence before suggesting fixes

1. **Read the logs** — Python logging writes to stdout in the format `LEVEL:logger:message`.
   Look for `ERROR` and `WARNING` lines:
   ```bash
   # Adjust the run command to match the actual entry point and venv location
   PYTHONPATH=src venv/bin/python -m app 2>&1 | grep -E "ERROR|WARNING"
   ```
2. **Enable gRPC interceptor debug logging** by setting in `.env`:
   ```dotenv
   PLUGIN_GRPC_SERVER_LOGGING_ENABLED=true
   ```
3. **Read the relevant source files** — use `Read` and `Grep` on files referenced in the
   traceback before suggesting any change.
4. **Check the environment:**
   ```bash
   printenv | grep -E 'AB_|PORT|ENABLE_|PLUGIN_|OTEL|PROMETHEUS'
   ```
5. **Check the ports:**
   ```bash
   ss -tlnp | grep -E '6565|8080'
   ```

### Step 3 — Common issues checklist

| Symptom | Likely cause | Where to look |
|---|---|---|
| `ERROR: <VAR> environment variable is required` then exit | App-specific required env var missing | Entry point — look for `env.str(...)` or `os.getenv(...)` followed by `sys.exit` |
| Exception from SDK login call | Wrong credentials or unreachable `AB_BASE_URL` | Entry point → `login_client` or equivalent; verify `AB_BASE_URL` with `curl` |
| `OnMessage` request log appears but no response log | Handler failed mid-execution | Handler file — inspect the error return / exception path |
| gRPC returns `INTERNAL`, no `ERROR` log | Exception caught before logger | Set breakpoint at the SDK call; enable `PLUGIN_GRPC_SERVER_LOGGING_ENABLED=true` |
| `OnMessage` never called | Namespace mismatch or handler not registered | Entry point → service registrations; check `AB_NAMESPACE` vs payload `namespace` field |
| Proto changes have no effect | Generated stubs not regenerated | Run the proto generation script (e.g., `./proto.sh`, `make proto`) and restart |
| Port conflict — "address already in use" | Another process on 6565 or 8080 | `ss -tlnp \| grep -E '6565\|8080'` |
| `grpcurl` returns "Failed to dial" | Server not started or crashed on startup | Check logs for `ERROR` lines; `ss -tlnp \| grep 6565` |
| Breakpoints never hit | Service started with the run task, not the debugger | Use VS Code **debug launch config** (F5), not the run task |

### Step 4 — Suggest a minimal, targeted fix

- Explain **why** the fix works, not just **what** to change.
- Read the relevant file first, then show the exact change needed.
- For environment issues, show the exact `.env` line to add or change.
- After suggesting a fix, provide a concrete verification step.

### Step 5 — Verify the fix

```bash
# Confirm service starts without errors (adjust run command to match the repo)
PYTHONPATH=src venv/bin/python -m app 2>&1 | grep -v "^INFO"

# Confirm gRPC server is listening
ss -tlnp | grep 6565

# List all registered gRPC services (gRPC reflection must be enabled — default: true)
grpcurl -plaintext localhost:6565 list

# Describe a handler method (replace with the actual service name from grpcurl list)
grpcurl -plaintext localhost:6565 describe <ServiceName>.OnMessage

# Manually invoke OnMessage (replace service name and payload fields from the proto)
grpcurl -plaintext \
  -d '{"userId": "test-user-001", "namespace": "mygame"}' \
  localhost:6565 \
  <ServiceName>/OnMessage
# Expected: {}

# Check Prometheus metrics
curl -s http://localhost:8080/metrics | grep grpc_server
```

---

## Write Mode

When writing or updating `DEBUGGING_GUIDE.md`, follow these principles.

### Audience

The guide targets **junior developers and game developers** with limited backend experience.
Avoid assuming prior knowledge of gRPC, protobuf, or event-driven systems. Use plain
language. The guide should be VS Code-centric but include notes for other editors.

### Required sections

A complete `DEBUGGING_GUIDE.md` must cover all of the following:

1. **Overview** — What the service does; the event-driven architecture diagram.
2. **Architecture Reference** — File/package responsibility table (derived from this repo);
   port map.
3. **Prerequisites** — Python version (check `runtime.txt`, `pyproject.toml`, or
   `Dockerfile`); venv setup; VS Code Python extension; debugpy; grpcurl. Use exact
   versions found in `requirements-dev.txt`.
4. **Environment Setup** — How to create `.env` from `.env.template`; all required
   variables with purpose; app-specific required vars called out explicitly as hard
   dependencies that will cause `sys.exit(1)` if missing.
5. **Running the Service** — Terminal command and VS Code task (use the actual task name
   from `.vscode/tasks.json`).
6. **Attaching the Debugger** — VS Code launch config (use the exact config name from
   `.vscode/launch.json`); headless debugpy steps for other IDEs.
7. **Breakpoints and Inspection** — Where to place them (handler entry, SDK call, error
   paths); stepping shortcuts; conditional breakpoint syntax (Python expressions).
8. **Reading Logs** — Python logging format (`LEVEL:logger:message`); filtering with
   `grep`; enabling `PLUGIN_GRPC_SERVER_LOGGING_ENABLED=true` for gRPC interceptor logs.
9. **Common Issues** — Each issue as a subsection: symptom → cause → fix.
10. **Testing Event Handlers Manually** — `grpcurl` to invoke `OnMessage`; discovering
    service names via gRPC reflection (`grpcurl -plaintext localhost:6565 list`).
11. **Prometheus Metrics** — What is exposed on `:8080/metrics`; `PROMETHEUS_PORT` override.
12. **Distributed Tracing** — Zipkin via `OTEL_EXPORTER_ZIPKIN_ENDPOINT`; how trace IDs
    flow from the AGS event payload through to OTEL spans.
13. **Adding a New Event Handler** — Steps: find the target service in the proto file,
    implement a new Servicer subclass, register it in the entry point with
    `AppGRPCServiceOpt`, regenerate stubs with the proto generation script.
14. **AI-Assisted Debugging** — MCP servers present in `.vscode/mcp.json`; effective
    prompting patterns.
15. **Tips and Best Practices** — Concise bullets.
16. **References** — Links to official AccelByte Extend docs.

### Style rules

- Use tables for structured comparisons (file maps, port maps, issue checklists, shortcuts).
- Use fenced code blocks with language tags for all code, commands, and log samples.
- Use `>` blockquotes for important warnings (e.g., "service exits immediately if a
  required env var is unset").
- Keep each section self-contained — a reader should jump to section 9 without reading 1–8.
- Do not exceed ~500 lines for the main guide. Move lengthy reference material to supporting
  files.
- Always link to official AccelByte docs at the end:
  - https://docs.accelbyte.io/gaming-services/modules/foundations/extend/
  - https://docs.accelbyte.io/gaming-services/modules/foundations/extend/event-handler/

### Before writing, always read the codebase first

Do not assume file names, env var names, or proto service names. Discover them:

1. Read any existing `DEBUGGING_GUIDE.md` — update it; don't replace accurate content.
2. Run the codebase discovery searches from the *"How to discover this codebase's layout"*
   section above to find the entry point, handler files, env var names, and port constants.
3. Read the entry point — extract port constants, hard-exit env var guards, and handler
   registration calls.
4. List and read the handler files — understand what events are handled and what downstream
   calls are made.
5. Read `.vscode/launch.json` — use the exact debug configuration name in the guide.
6. Read `.vscode/mcp.json` — list the actual MCP servers configured (for section 14).
7. Find and read the proto files — list the gRPC service names that are actually registered.
8. Check for a proto generation script (`proto.sh`, `Makefile`, etc.) — use the real command.
9. Check `.env.template` — use its variable names verbatim in the guide.

---

## Python-Specific Event Handler Patterns

### Entry point structure

Most Python Extend Event Handler entry points follow this pattern — verify the actual file:

```python
async def main(**kwargs) -> None:
    env = create_env(**kwargs)          # loads .env file via environs
    # ... SDK init, IAM login ...
    _, error = auth_service.login_client(sdk=sdk)
    if error:
        raise Exception(error)          # or sys.exit

    # app-specific required vars validated here — these are hard dependencies
    some_var = env.str("SOME_VAR", None)
    if not some_var:
        logger.error("SOME_VAR environment variable is required")
        sys.exit(1)

    # handler registration
    opts.append(AppGRPCServiceOpt(MyHandlerService(...), ...))
    app = App(port=port, env=env, logger=logger, opts=opts)
    await app.run()
```

When debugging startup failures, read the entry point top-to-bottom — the exact error
message is almost always printed before `sys.exit(1)`.

### Handler namespace guard

Many handlers silently return `Empty()` for events from other namespaces:

```python
async def OnMessage(self, request, context):
    if request.namespace != self.namespace:
        return Empty()  # ← silent no-op — no error, no downstream action
    # ... business logic ...
```

This is intentional but is a common source of "nothing happens" confusion when testing.
Always match the `namespace` field in `grpcurl` payloads to `AB_NAMESPACE`.

### Error return convention

Many Python Extend Event Handler implementations use return-value error signalling rather
than exceptions in downstream helpers:

```python
# helper returns Optional[Exception]
error = some_helper(...)
if error:
    await context.abort(grpc.StatusCode.INTERNAL, str(error))
    return
```

When debugging a silent failure, inspect the `error` return value at the call site — do not
assume a failed downstream call will automatically produce a log line or raised exception.

### Log format

Python's standard `logging` module produces plain-text lines:

```
INFO:app:OnMessage request: {"user_id": "test-user-001", "namespace": "mygame"}
INFO:app:OnMessage response: {}
```

There is no JSON structure. Filter with `grep`:

```bash
# Adjust the run command to match the actual entry point and venv location
PYTHONPATH=src venv/bin/python -m app 2>&1 | grep "ERROR"

# Show all OnMessage calls
PYTHONPATH=src venv/bin/python -m app 2>&1 | grep "OnMessage"
```

A successful handler call produces a request log **and** a response log. If only the
request line appears with no response line, the handler encountered an error before
returning — look for `ERROR` lines in the same output.

### Attaching debugpy (headless, for non-VS Code IDEs)

```bash
export $(grep -v '^#' .env | xargs)
PYTHONPATH=src venv/bin/python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m app
```

The process blocks until a debugger connects via DAP (Debug Adapter Protocol) on port 5678.

### gRPC reflection

If `ENABLE_REFLECTION=true` (the default), `grpcurl` works without a `.proto` file:

```bash
grpcurl -plaintext localhost:6565 list
```

This is the fastest way to verify that the server is up and that the expected services are
registered.

---

## Supporting files in this skill

- See [examples/debug-startup-failure.md](examples/debug-startup-failure.md) for an
  annotated example of diagnosing an immediate startup exit caused by a missing required
  env var.
- See [examples/debug-silent-handler-failure.md](examples/debug-silent-handler-failure.md)
  for an annotated example of a handler that receives events and returns `OK` but silently
  performs no action — and how to surface and fix the root cause.

---

### App-specific required env vars

Beyond the standard `AB_*` variables, most apps require one or more domain-specific env
vars (item IDs, feature flags, external endpoints). Read the entry point to find every
`env.str(...)` or `os.getenv(...)` call followed by `sys.exit`, `raise`, or a fatal log on
an empty value — those are hard dependencies that must be called out in the guide's
Environment Setup section.
