# The Broken Gate — operator notebook

## Hypothesis

The sample appears to implement a local feature gate. The initial indicators
are the `license`, `premium`, `accepted` and `rejected` strings, plus the
Windows identity API imported by the executable.

## Observation

The program accepts a license-like value, derives a local decision and prints a
training token on success. The token is deliberately synthetic. No network
request is made and no external service is involved.

The important observation is architectural: the decision is made entirely in
the client process. A local boolean is treated as proof of authorization.

## Validation flow

```text
input
  ↓
normalize
  ↓
local license comparison
  ├─ mismatch → rejected
  └─ match    → accepted → synthetic training token
```

The relevant branch is easy to locate because the sample contains distinct
success and failure strings. In a real assessment, strings are only anchors:
the conclusion must be supported by the instructions that produce the branch
and by runtime observation in an authorized environment.

## Finding

**Local validation is not an authorization boundary.**

The client can be inspected and modified by the same party who controls the
process. This makes the local result suitable for user experience, but not for
protecting a premium capability or sensitive resource.

## Engineering fix

Move the trust decision to a service-side verifier:

1. send a short-lived, audience-bound request to the service;
2. verify entitlement server-side;
3. return the minimum capability needed for the current operation;
4. bind sensitive operations to a server-issued, expiring token;
5. treat every client-side check as advisory only.

## Evidence standard

This lab intentionally records the reasoning rather than publishing a patch
against third-party software. The conclusion is reproducible from the source,
the generated sample and the inspection tooling in this repository.

## Operator takeaway

The strongest result is not changing a string or forcing a branch. It is
identifying the trust-boundary failure, proving it with minimal evidence and
explaining the design that removes the weakness.
