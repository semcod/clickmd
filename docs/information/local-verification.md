---
{
  "schema": "wellmanifest.docs/document/v1",
  "id": "local-verification",
  "kind": "information",
  "version": 1,
  "title": "Protected local verification for Clickmd",
  "status": "proposed",
  "owner": "semcod/clickmd",
  "created": "2026-09-08",
  "updated": "2026-09-08",
  "review_after": "2026-09-15",
  "source_revision": "b8720fb50d63103007e229872c92c190d7fa326e",
  "affected_repositories": [
    "semcod/clickmd"
  ],
  "evidence": [
    "https://github.com/subactor/onedev-agent/pull/202",
    "https://github.com/semcod/clickmd/issues/4"
  ]
}
---

# Protected local verification

<!-- docs:section purpose -->
## Purpose

Verify the complete Clickmd test suite in the independent local executor while
preserving the existing required hosted Python matrix. This repository adopts
Wellmanifest Docs metadata for authored information through `.governance/docs.json`.

<!-- docs:section scope -->
## Scope

The local profile runs Python 3.10.19 and 3.13.15 with the same locked dev,
click and rich extras as `.github/workflows/test-locked.yml`. The protected
image prepares dependencies before candidate execution; both test runs are
networkless. A second gate runs the pinned documentation checker against the
trusted current base. The OneDev deployment is owned by subactor/onedev-agent.

<!-- docs:section evidence -->
## Evidence

An offline image canary of the bound source passed 66 tests on each Python,
with three existing absent-Click cases skipped because the required Click
extra is installed. The executor's regression suite rejects altered, missing
or symlinked dependency inputs and propagates failures from either interpreter.
This document and pin form the real consumer PR canary after executor deployment.
Its terminal receipt determines publication success; the document does not
approve itself.

<!-- docs:section content -->
## Contract

The executor compares candidate `pyproject.toml` and `uv.lock` to independently
approved digests. A change requires an explicit executor package update before
publication can pass. The candidate cannot introduce new trusted pins.
Each Python imports Clickmd from this checkout's `src`, validates the source
path and runs the complete pytest suite. This validates source behavior, not
wheel packaging or every IDE/LLM integration.

OneDev reports the existing `onedev/local-verify` status. The protected
Validator continues requiring both hosted `test (3.10)` and `test (3.13)`;
the new local result does not silently replace them. Independent exact-head
review and an explicit merge grant remain separate publication requirements.

<!-- docs:section limitations -->
## Limits

This is a Linux matrix. It does not certify Windows, macOS, GUI integrations,
LLM correctness or deployed product behavior. The three skipped tests cover
an environment without Click; they are not runtime test failures.
The documentation pin declares adoption. Actual enforcement additionally
requires the deployed protected checker and a successful exact-base PR receipt.

<!-- docs:section next_actions -->
## Acceptance

Publish after both hosted tests, the deployed local matrix and documentation
gate pass. Preserve the exact head/base/merge evidence in the independent
receipt. Future dependency changes must update the protected image through
its own reviewed source, test and deployment process.
