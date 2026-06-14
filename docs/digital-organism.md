# The Digital Organism Model

> Stop thinking "a script that calls an LLM". Start thinking "a living system
> that senses, reasons, proposes, acts and learns — under a human's authority".

## One-shot agents vs. an organism

A typical agent:

```
prompt → LLM → output → done
```

It is stateless, brittle, and ungovernable. The moment you have several of them,
nobody knows what happened, why, or what it cost.

A **digital organism** runs in **closed loops**:

```
sense → reason → propose → (human gate) → act → observe outcome → learn
        ↑                                                            │
        └──────────────────────── memory ───────────────────────────┘
```

Every cycle leaves a trace. Outcomes feed back. The system gets *calibrated* by
reality instead of repeating the same mistakes.

## Organs

Functionality is split into **organs** — small, single-purpose modules with a
clear role, not a monolith:

| Organ (role) | Responsibility |
|---|---|
| **Sensors** | pull signals from the world (feeds, metrics, events) |
| **Brain** | decide what matters and what to do next |
| **Memory** | remember context, decisions and outcomes |
| **Immune system** | detect and block harmful states |
| **Conscience / policy** | enforce what must never happen |
| **Reproductive / codegen** | spawn new organs or projects (on review) |
| **Voice** | talk to the human (briefings, questions, alerts) |

Organs don't call each other directly. They communicate through **events** (see
[harness-protocol](harness-protocol.md)) and a shared **meta-field** (see
[meta-field](meta-field.md)).

## "Hormones": adaptive thresholds

Instead of hard-coded constants, an organism keeps a few global **state
variables** (call them hormones) that shift its behaviour:

- a *stress* level that raises caution and slows risky actions,
- a *reward* level that reinforces what worked,
- a *rest* level that throttles activity when nothing is urgent.

These are just bounded numbers updated from real events — but they let the same
code behave calmly in normal times and conservatively under pressure, without
rewrites.

## Why this matters

- **Resilience** — a swallowed exception or a dead loop leaves a trace, not
  silence.
- **Governability** — there is always a record and a boundary.
- **Adaptivity** — outcomes calibrate confidence over time.
- **Composability** — new organs plug into the same event + field substrate.

The contract that makes any system a well-behaved organ is the
**[Organism Harness Protocol](harness-protocol.md)**.
