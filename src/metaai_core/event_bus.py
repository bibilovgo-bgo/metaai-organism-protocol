"""In-memory pub/sub event bus.

Organism elements react to events — they never call each other directly. This
removes hard coupling: a new element can subscribe to existing events without
anyone wiring it in.
"""

import itertools
from collections import defaultdict
from datetime import datetime, timezone
from types import SimpleNamespace


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class EventBus:
    def __init__(self) -> None:
        self._subs: dict[str, list] = defaultdict(list)
        self._log: list[dict] = []
        self._ids = itertools.count(1)

    def subscribe(self, event_type: str, handler) -> None:
        """Register a handler(event) for an event type."""
        self._subs[event_type].append(handler)

    def emit(
        self,
        event_type: str,
        payload: dict | None = None,
        source: str = "",
        trace_id: str = "",
    ) -> dict:
        """Publish an event and synchronously notify subscribers."""
        ev = {
            "id": next(self._ids),
            "type": event_type,
            "payload": payload or {},
            "source": source,
            "ts": _now(),
            "trace_id": trace_id,
        }
        self._log.append(ev)
        for handler in list(self._subs.get(event_type, [])):
            handler(SimpleNamespace(**ev))
        return ev

    def recent(self, n: int = 50) -> list[dict]:
        """Most recent events, newest first."""
        return self._log[-n:][::-1]
