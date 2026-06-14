# The Decision Ledger

> If decisions live in chat, they are lost. The ledger makes every consequential
> decision **explicit, attributed, and checked against its outcome.**

## The problem

In most teams (and most agent systems) decisions happen verbally or implicitly:

- no record of *why* something was decided,
- no owner,
- no follow-up on whether it worked,
- the same mistakes repeat.

## The ledger entry

Every decision is a row (see
[`schemas/decision.schema.yaml`](../schemas/decision.schema.yaml)):

| Field | Meaning |
|---|---|
| `title` | what is being decided |
| `rationale` | why — the reasoning at the time |
| `confidence` | 0..1, how sure |
| `decided_by` | human / which organ |
| `status` | pending / approved / rejected / reversed |
| `outcome` | what actually happened (won / lost / wip) |
| `outcome_value` | measured result, when known |

Because the rationale and confidence are stored **at decision time**, you can
later compare predicted vs. actual and **calibrate** the system's confidence.

## Outcomes feed learning

```
decision → action → real outcome → update confidence for similar future decisions
```

A decision that was approved with 0.6 confidence and lost teaches the organism
to be more cautious about that pattern. This is how the organism stops repeating
mistakes.

## The Rejection Re-examiner ("anti-mirror in time")

A rejected idea is not always wrong forever — sometimes reality changes. But
re-proposing it immediately is spam.

The re-examiner:

1. lets a rejected decision **mature** (a cooldown),
2. re-evaluates it later *from the height of new reality*,
3. only re-surfaces it if conditions genuinely changed,
4. and **never** re-surfaces something the human marked "won't do".

This respects the human's "no" while still catching the case where a once-bad
idea has become a good one.
