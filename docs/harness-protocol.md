# The Organism Harness Protocol

> A **harness** turns any system — an agent, a script, a third-party service —
> into a *governed element*: it declares what it can do, what it needs, what it
> emits, and what it must never do.

A harness is not an integration. An integration just connects A to B. A harness
**tames** a system: it adds capabilities, permissions, events, health, rollback,
a human gate and policy around it.

## The harness manifest

Every harnessed element ships a small, declarative manifest
(see [`schemas/harness_manifest.schema.yaml`](../schemas/harness_manifest.schema.yaml)):

```yaml
name: seller_command_center
role: operator            # scout | judge | builder | operator | treasurer | ...
i_can:
  - analyze_reviews
  - generate_offer
  - detect_risk
i_need:
  - marketplace_data
  - pricing_rules
i_emit:
  - insight.generated
  - risk.detected
  - action.proposed
i_must_not:
  - spend_money
  - contact_client_without_approval
autonomy: recommend       # see human-gate.md
health_check: /healthz
rollback: supported
```

This is a **social contract for a system**, not just an API surface.

## What a harness provides

| Facet | Meaning |
|---|---|
| **Capabilities** | what the element is allowed to attempt (`i_can`) |
| **Dependencies** | what it needs to function (`i_need`) |
| **Events** | what it publishes to the bus (`i_emit`) |
| **Forbidden** | hard limits, enforced by policy (`i_must_not`) |
| **Autonomy level** | how far it may act alone (observe → execute) |
| **Health** | liveness/heartbeat so the organism knows it's alive |
| **Rollback** | how to undo, when undo is possible |

## Events, not commands

Harnessed elements talk through an **event bus**. Instead of `A.call(B)`:

```
A emits  lead.found
B (subscribed to lead.found) decides whether it's relevant and reacts
```

This removes hard coupling: changing one element doesn't break another, and new
elements can subscribe to existing events without anyone wiring them in.

## Harness-of-harnesses

When you have many harnessed systems, a **meta-control plane** governs them:
who is connected, who is alive, who is useful, who is costly, who to amplify,
who to retire. Above that sits the **[meta-field](meta-field.md)** — coordination
through a shared picture of reality rather than direct orchestration.
