# The Human Gate & Graduated Autonomy

> The organism may think, plan and prepare freely — but it must ask a human
> before anything irreversible. Authority stays with the owner.

## Autonomy levels

Not every action carries the same risk. The protocol defines graduated levels;
each capability in a [harness manifest](harness-protocol.md) declares the highest
level it is allowed to reach.

| Level | The AI may… | Gate |
|---|---|---|
| **observe** | read, collect signals | auto |
| **summarize** | produce briefings | auto |
| **recommend** | propose actions | auto |
| **prepare / draft** | write the text/task/plan (not send it) | auto |
| **execute-reversible** | take undoable actions | limited auto |
| **execute-irreversible** | money, external messages, prod, deletes | **human confirm** |
| **self-modify** | change its own rules/code | **human confirm + tests** |

On a first deployment, almost everything sits at **observe → recommend → draft**.
The AI makes the work *visible* and *prepared*; the human keeps the trigger.

## The gate in practice

```
organ proposes  →  decision ledger entry (pending)
                →  human sees it in a briefing
                →  approve / reject / "won't do"
                →  only then does an executor act
```

The human is never spammed with noise: low-risk items flow automatically, and
only genuine decisions reach them — ideally as a short daily briefing, not a
firehose.

## The Meta-Constitution

Above individual gates sits a small **constitution**
(see [`schemas/constitution.schema.yaml`](../schemas/constitution.schema.yaml)) —
the rules the organism can never override:

```yaml
prime_directives:
  - preserve_human_authority
  - prevent_irreversible_harm
  - maximize_useful_outcomes
  - minimize_cost_and_noise
  - preserve_memory_integrity
forbidden:
  - spend_money_without_approval
  - contact_external_parties_without_gate
  - modify_production_without_review
  - delete_data_without_snapshot
autonomy_defaults:
  execute_irreversible: human_confirm
  self_modify: human_confirm_plus_tests
```

This is what makes growing autonomy **safe**: the more the organism can do, the
more clearly its hard limits and human gates are defined.
