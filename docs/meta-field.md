# The Meta-Field

> The highest-leverage idea: systems should coordinate not through commands and
> events alone, but through a shared **field of reality**. A system changes the
> field; other systems see the change and decide for themselves whether it
> concerns them.

## From commands to a field

```
Direct:   System A → "do X" → System B          (tight coupling, fragile)
Field:    System A changes the field
          System B sees the change and reacts on its own terms
```

This is how a city works: there is no API between all people — there are roads,
prices, laws, signals, news. Coordination emerges from a shared environment.

## What the field holds

| Field | Holds |
|---|---|
| `reality` | facts about the world (projects, systems, money, status) |
| `goals` | active goals and priorities |
| `risks` | current threats |
| `opportunities` | openings worth acting on |
| `attention` | what matters *right now* |
| `economy` | cost, value, ROI, noise per element |
| `trust` | reputation of systems, agents, data sources |
| `decisions` | what is pending, approved, rejected, reversed, learned |

## Example

One system writes a change to the field:

```json
{
  "field": "business_reality",
  "change": "MRR_growth_stalled",
  "severity": "high",
  "related": ["product_x", "product_y"],
  "possible_causes": ["no_outreach", "weak_offer", "no_payment_link"]
}
```

Nobody is commanded. But independently:

- a marketing organ drafts an offer,
- a finance organ checks pricing,
- a risk organ verifies constraints,
- the **human gate** surfaces a decision to the owner,
- memory records whatever outcome follows.

They all reacted to a **change in the field**.

## Why it scales

Point-to-point orchestration grows as *O(n²)* connections. A shared field grows
as *O(n)* — each system only needs to read the field and publish its own
changes. New systems join by reading the same reality, not by being wired to
every existing one.
