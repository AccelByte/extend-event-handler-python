# Example: Service Exits Immediately at Startup

This annotated example shows a debugging session where the Extend Event Handler process
exits right after launch with no gRPC server ever starting.

> **This is an illustrative example.** Variable names, file paths, and log messages will
> differ across repos. Always read the actual entry point to find the real values.

---

## The Report

A developer sends this message:

> *"I run the app and the process just quits. Nothing happens, no server, no useful output.
> I set up `.env` from the template."*

---

## Step 1 — Read the exit output carefully

Ask the developer to share the full terminal output. They share:

```
INFO:app:login client...
INFO:app:login client successful
ERROR:app:SOME_REQUIRED_VAR environment variable is required
```

**What this tells us:**

- The standard `AB_*` credentials are valid — the IAM login succeeded.
- The process hit an app-specific env var validation block in the entry point.
- `sys.exit(1)` was called before the gRPC server ever started.

Note: if the IAM login itself had failed, the error would mention credentials or
`AB_BASE_URL` instead. This particular message points to a domain-specific required
variable that the template did not fill in.

---

## Step 2 — Find the validation in the entry point

Read the entry point (typically `__main__.py` or `main.py`) to confirm what the service
expects. Look for patterns like:

```python
some_var = env.str("SOME_REQUIRED_VAR", None)
if not some_var:
    logger.error("SOME_REQUIRED_VAR environment variable is required")
    sys.exit(1)
```

or:

```python
some_var = os.environ.get("SOME_REQUIRED_VAR")
if not some_var:
    raise RuntimeError("SOME_REQUIRED_VAR is required")
```

**Problem identified:** `.env.template` lists `SOME_REQUIRED_VAR=` or
`SOME_REQUIRED_VAR='placeholder'` as an unfilled entry, and the developer copied it without
supplying a real value.

---

## Step 3 — Check the .env file

```bash
# Replace SOME_REQUIRED_VAR with the actual variable name from the error message
grep SOME_REQUIRED_VAR .env
# Output: SOME_REQUIRED_VAR=  (empty or placeholder)
```

Confirmed — the value is missing or still a placeholder.

---

## Step 4 — The fix

Open `.env` and set the real value. For example, if the variable is an item ID from AGS:

```dotenv
SOME_REQUIRED_VAR=a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

Where to find the correct value depends on the variable:
- Item or SKU IDs: AGS Publisher Portal → Game Management → Items
- Namespace: AGS Admin Portal → namespace settings
- External service URLs: the README or infrastructure docs for the target environment

> **Important:** Every app-specific required variable must be filled in before the service
> can start. Check `.env.template` for all variables with empty or placeholder values and
> confirm you have a real value for each one before running for the first time.

---

## Step 5 — Verify

Restart the service. Expected startup output (no exit):

```
INFO:app:login client...
INFO:app:login client successful
INFO:app:starting app server..
INFO:app:gRPC health checking enabled
INFO:app:gRPC reflection enabled
INFO:app:prometheus enabled
INFO:app:zipkin enabled
INFO:app:app server started
```

Confirm the gRPC server is up:

```bash
ss -tlnp | grep 6565
# Expected: LISTEN ... :6565

# List registered services (gRPC reflection must be enabled — default: true)
grpcurl -plaintext localhost:6565 list
```

---

## Key takeaways from this session

1. **The first `ERROR` log line is the diagnosis.** Python logs the exact missing variable
   name before exiting — no debugger needed.
2. **Successful IAM login does not mean all vars are set.** `AB_*` credentials are
   validated at parse time, but app-specific vars are checked separately — later in
   `main()`. A successful login does not guarantee the remaining checks will pass.
3. **`.env.template` placeholder values are not defaults** — they will cause `sys.exit(1)`.
   Fill every empty or placeholder value before running the service for the first time.
4. **Read the entry point top-to-bottom** to discover all hard-exit env var guards. Look
   for `env.str(...)` or `os.getenv(...)` assignments followed by `if not ...: sys.exit(1)`
   or `raise`. Those are the complete list of required variables for this app.
