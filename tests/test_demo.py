"""The full loop, end to end: tick -> proposal -> human gate -> act -> outcome."""

from src.metaai_core.organism import Organism
from src.metaai_core.policy import is_forbidden, requires_human


def test_tick_creates_a_pending_decision():
    org = Organism()
    org.tick()
    pending = org.ledger.pending()
    assert len(pending) == 1
    assert pending[0]["status"] == "pending"
    assert 0.0 <= pending[0]["confidence"] <= 1.0


def test_approve_runs_operator_and_records_outcome():
    org = Organism()
    org.tick()
    did = org.ledger.pending()[0]["id"]
    org.approve(did)
    row = next(r for r in org.ledger.all() if r["id"] == did)
    assert row["status"] == "approved"
    assert row["outcome"] == "wip"  # operator reacted to decision.approved
    assert any(e["type"] == "action.executed" for e in org.bus.recent())


def test_wont_do_is_marked_and_not_resurfaced():
    org = Organism()
    org.tick()
    did = org.ledger.pending()[0]["id"]
    org.reject(did, note="not now", wont_do=True)
    row = next(r for r in org.ledger.all() if r["id"] == did)
    assert row["status"] == "rejected"
    assert row["wont_do"] is True


def test_constitution_human_gate():
    assert requires_human("execute_irreversible") is True
    assert requires_human("observe") is False
    assert is_forbidden("spend_money_without_approval") is True
