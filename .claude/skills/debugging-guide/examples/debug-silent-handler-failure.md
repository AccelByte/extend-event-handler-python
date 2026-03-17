# Example: Handler Called but Downstream Action Not Performed

This annotated example shows a debugging session where events are being received and logged,
but the downstream action (e.g., granting an entitlement, writing a record) silently does
nothing.

> **This is an illustrative example.** The specific handler names, helper functions, and
> variable names will differ across repos. The diagnostic patterns are universal.

---

## The Report

A developer sends this message:

> *"The service is running and I can see in the logs that `OnMessage` is being called, but
> the action never happens. No errors in the logs either."*

---

## Step 1 — Read the logs carefully

The developer shares:

```
INFO:app:OnMessage request: {"user_id": "user-xyz", "namespace": "mygame"}
INFO:app:OnMessage response: {}
```

**What this tells us:**

- The event was received and `OnMessage` returned successfully (response logged as `{}`).
- There is no `ERROR` line — but also no log confirming the action was performed.
- The handler completed without error, yet the action didn't happen. This points to a
  silent failure or a missing log inside the downstream helper.

---

## Step 2 — Check for a namespace mismatch

Before inspecting business logic, check the most common cause of silent no-ops in Python
Extend Event Handler apps. Many handlers guard against foreign-namespace events:

```python
async def OnMessage(self, request, context):
    # log the request...

    if request.namespace != self.namespace:
        return Empty()  # ← silent return, no error, no downstream action

    # ... business logic ...
```

Ask the developer: **what value did they use for `namespace` in the `grpcurl` payload?**
If it does not exactly match `AB_NAMESPACE` in `.env`, the handler returns early and the
downstream action is never attempted.

**Quick test:** Use `grpcurl` with the exact `AB_NAMESPACE` value from `.env`:

```bash
# Use the actual service name from: grpcurl -plaintext localhost:6565 list
# Use the actual AB_NAMESPACE value from your .env
grpcurl -plaintext \
  -d '{"userId": "test-user-001", "namespace": "<AB_NAMESPACE>"}' \
  localhost:6565 \
  <ServiceName>/OnMessage
```

If the namespace was wrong, correcting it resolves the issue immediately.

---

## Step 3 — Inspect the business logic

If the namespace is correct, read the handler's `OnMessage` and the downstream helper it
calls. Look for this pattern:

```python
# The handler calls a helper that returns Optional[Exception]
error = some_downstream_helper(...)
if error:
    await context.abort(grpc.StatusCode.INTERNAL, str(error))
    return

response = Empty()
# log the response...
return response
```

**The handler only aborts with `INTERNAL` if `error` is truthy.** If the helper returns
`None`, the response is `{}` regardless of whether the action actually succeeded. This
means a silent failure inside the helper (e.g., an empty result from the SDK) is invisible
at the handler level.

Read the helper function and check whether it can return `None` (success) in situations
where the desired action was not actually performed — for example, when the SDK returns
an empty result list instead of raising an error.

---

## Step 4 — Confirm with a breakpoint

Find the `error = some_downstream_helper(...)` call site in the handler file and set a
breakpoint on the line immediately after:

```python
error = some_downstream_helper(...)
# ← set breakpoint here
if error:
```

1. Launch via the VS Code debug launch config (F5).
2. Send a `grpcurl` request to trigger the event.
3. When the breakpoint hits, inspect `error` in the **Variables** panel:
   - If `error` is not `None`, the downstream call failed — read the exception message.
   - If `error` is `None`, step into the helper and inspect its internal state — look for
     an SDK result with an empty or unexpected payload.

Also inspect any ID or configuration variables the handler passes to the helper — a typo
or wrong UUID in the `.env` file is a common root cause.

---

## Step 5 — Root cause and fix

The two most common root causes:

**Configuration mismatch:** The ID or setting passed to the downstream API is valid in the
catalogue but not configured correctly for the target namespace/environment. Fix it in the
corresponding AGS portal or admin interface.

**Wrong value in `.env`:** An app-specific variable (e.g., an item ID or external endpoint)
contains a typo or points to the wrong environment.

```bash
# Print all app-specific env vars to verify their values
printenv | grep -v '^AB_\|^ENABLE_\|^PLUGIN_\|^OTEL\|^PROMETHEUS'
```

Compare each value against what is actually configured in your AGS environment.

---

## Step 6 — Verify

After the fix, send the same `grpcurl` request again. Both a request log and a response
log should appear:

```
INFO:app:OnMessage request: {"user_id": "test-user-001", "namespace": "mygame"}
INFO:app:OnMessage response: {}
```

Confirm the downstream action took effect via the AGS portal or the relevant API.

---

## Key takeaways from this session

1. **`{}` response does not mean the business action succeeded.** Both a successful action
   and a namespace-mismatch early-return produce the same `{}` output. Always confirm the
   result in the downstream system.
2. **Namespace mismatch is the most common silent no-op.** Always set `"namespace"` in the
   `grpcurl` payload to the exact value of `AB_NAMESPACE`.
3. **Return-value error signalling makes failures silent.** When a helper returns
   `Optional[Exception]`, a failed SDK call that returns `None` (or an unexpected empty
   result) will not automatically produce a log line. Inspect the return value at the call
   site with a breakpoint.
4. **Set a breakpoint, don't guess.** The Variables panel shows the exact state of every
   local variable at runtime — far faster than adding print statements and restarting.
