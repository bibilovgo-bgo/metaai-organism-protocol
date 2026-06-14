"""Three minimal demo agents.

They communicate only through events on the bus — never by calling each other.

    Scout    senses the world and emits a raw signal.
    Judge    evaluates a signal, reasons, and PROPOSES a decision (human-gated).
    Operator acts ONLY on approved decisions, and never does forbidden things.
"""

from .mock_llm import reason
from .policy import is_forbidden


def scout_sense(bus) -> None:
    """Scout: emit one raw signal. (Demo: a canned marketplace signal.)"""
    bus.emit(
        "signal.found",
        {
            "topic": "marketplace_reviews",
            "text": "Several reviews complain about slow delivery on SKU-42.",
        },
        source="scout",
    )


def register(bus, ledger) -> None:
    """Wire Judge and Operator to the bus."""

    def judge(event) -> None:
        verdict = reason(
            "Propose ONE next action with a confidence.", context=event.payload
        )
        d = ledger.propose(
            title=f"Act on: {event.payload.get('topic', 'signal')}",
            rationale=verdict["rationale"],
            confidence=verdict["confidence"],
            source="judge",
        )
        bus.emit(
            "proposal.generated",
            {"decision_id": d["id"], "title": d["title"]},
            source="judge",
        )

    def operator(event) -> None:
        # Demonstrates the constitution: the operator refuses forbidden actions.
        if is_forbidden("spend_money_without_approval"):
            pass  # would never auto-spend; here we simply skip that path
        decision_id = event.payload.get("decision_id")
        bus.emit(
            "action.executed",
            {"decision_id": decision_id, "mode": "reversible"},
            source="operator",
        )
        ledger.record_outcome(decision_id, "wip")

    bus.subscribe("signal.found", judge)
    bus.subscribe("decision.approved", operator)
