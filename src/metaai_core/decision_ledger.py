"""Decision ledger.

Every consequential decision is recorded with rationale and confidence at the
time it is made, then checked against its real outcome. This is what lets an
organism calibrate its confidence and stop repeating mistakes.
"""

import itertools
from datetime import datetime, timezone


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class DecisionLedger:
    def __init__(self) -> None:
        self._rows: dict[int, dict] = {}
        self._ids = itertools.count(1)

    def propose(
        self, title: str, rationale: str, confidence: float, source: str = ""
    ) -> dict:
        i = next(self._ids)
        self._rows[i] = {
            "id": i,
            "title": title,
            "rationale": rationale,
            "confidence": round(float(confidence), 2),
            "decided_by": source,
            "status": "pending",
            "created_at": _now(),
            "decided_at": "",
            "note": "",
            "outcome": "",
            "outcome_value": 0.0,
            "wont_do": False,
        }
        return self._rows[i]

    def decide(
        self, decision_id: int, action: str, note: str = "", wont_do: bool = False
    ) -> dict:
        row = self._rows.get(decision_id)
        if row is None:
            return {"error": "decision not found"}
        if action not in ("approved", "rejected"):
            return {"error": "action must be 'approved' or 'rejected'"}
        row["status"] = action
        row["decided_at"] = _now()
        row["note"] = note
        row["wont_do"] = bool(wont_do and action == "rejected")
        return row

    def record_outcome(
        self, decision_id: int, outcome: str, value: float = 0.0
    ) -> dict | None:
        row = self._rows.get(decision_id)
        if row is not None:
            row["outcome"] = outcome
            row["outcome_value"] = float(value)
            row["outcome_at"] = _now()
        return row

    def pending(self) -> list[dict]:
        return [r for r in self._rows.values() if r["status"] == "pending"]

    def all(self) -> list[dict]:
        return list(self._rows.values())
