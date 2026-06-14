# METAai — Organism Harness Protocol

> **An open protocol for governing autonomous AI systems as digital organisms.**
> Not "build more agents" — *govern* the systems you already have: events,
> permissions, memory, a decision ledger, a human gate, and an economy of
> usefulness.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
&nbsp;Status: **v0.1.0 — public preview** · Author: **Georgiy Bibilov**

---

## Why

Most "AI agent" projects are one-shot prompt chains: brittle, stateless, and
impossible to govern. As soon as you have *several* systems — a sales bot, a
research agent, a deploy script, a dashboard — there is no shared picture, no
record of why decisions were made, no safe boundary on what AI may do alone.

**METAai** treats a portfolio of systems as a **digital organism**: agents and
"organs" live in closed loops (*sense → reason → propose → act → learn*),
coordinate through a shared field of reality, record every decision, and ask a
human before anything irreversible.

This repository is the **open core**: the protocol, the schemas, the concepts,
and a small runnable reference demo — enough to understand and adopt the model.

## What's inside

```
docs/        — the architecture, in plain language
  digital-organism.md      the organism model (loops, organs, hormones)
  harness-protocol.md      how a system becomes a governed element
  meta-field.md            coordination through a shared field, not commands
  decision-ledger.md       recording decisions + outcomes
  human-gate.md            graduated autonomy & human approval
schemas/     — machine-readable contracts (YAML/JSON Schema)
src/         — a minimal, self-contained reference runtime (FastAPI + demo)
examples/    — example harness manifests
```

## Quickstart (reference demo)

```bash
pip install -r requirements.txt
uvicorn src.metaai_core.app:app --reload
# open http://127.0.0.1:8000  — event bus, 3 demo agents, decision ledger, human gate
```

The demo is intentionally tiny and uses **mock data only**. It exists to show
the *shape* of the architecture, not to be a product.

## What this is **not**

This repo is **not** the live, commercial METAai. The production organism — its
real agents, prompts, business strategy, revenue logic, integrations and
infrastructure — is private and stays private. Here you get the **governed
architecture and protocol**, not the brain.

## Authorship

The architecture, terminology and protocol here were created by
**Georgiy Bibilov (Георгий Бибилов)**. See [`PRIORITY_STATEMENT.md`](PRIORITY_STATEMENT.md)
and [`CITATION.cff`](CITATION.cff). First public release: **2026-06-14**.

## License

[Apache License 2.0](LICENSE) — free to use, including commercially, with
attribution and a patent grant.
