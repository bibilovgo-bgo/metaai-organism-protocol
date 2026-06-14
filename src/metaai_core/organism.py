"""The organism: wires the bus, the ledger and the demo agents into one loop.

tick()    -> sense -> reason -> propose (a decision lands as 'pending')
approve() -> human gate opens -> operator acts -> outcome recorded
reject()  -> decision closed; with wont_do=True it is never resurfaced
"""

from . import agents
from .decision_ledger import DecisionLedger
from .event_bus import EventBus


class Organism:
    def __init__(self) -> None:
        self.bus = EventBus()
        self.ledger = DecisionLedger()
        agents.register(self.bus, self.ledger)

    def tick(self) -> None:
        """Run one sense -> reason -> propose cycle."""
        agents.scout_sense(self.bus)

    def approve(self, decision_id: int, note: str = "") -> dict:
        row = self.ledger.decide(decision_id, "approved", note)
        if row.get("status") == "approved":
            self.bus.emit(
                "decision.approved", {"decision_id": decision_id}, source="human"
            )
        return row

    def reject(self, decision_id: int, note: str = "", wont_do: bool = False) -> dict:
        return self.ledger.decide(decision_id, "rejected", note, wont_do=wont_do)
