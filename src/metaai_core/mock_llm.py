"""Mock LLM.

The demo runs with NO API key. `reason()` returns deterministic, plausible
output so the architecture can be demonstrated offline. To use a real
OpenAI-compatible endpoint, set LLM_BASE_URL / LLM_API_KEY in .env and replace
this module's body — the rest of the organism does not change.
"""

import os


def reason(prompt: str, context: dict | None = None) -> dict:
    """Return a mock 'reasoning' result: a rationale and a confidence in 0..1."""
    ctx = context or {}
    topic = ctx.get("topic", "the signal")

    if os.environ.get("LLM_BASE_URL"):
        # A real implementation would call the configured endpoint here.
        # Kept as a no-op fallthrough so the demo never requires a key.
        pass

    return {
        "rationale": (
            f"The signal about '{topic}' looks like a recurring, fixable issue. "
            "A small reversible action now likely prevents a larger loss later."
        ),
        "confidence": 0.62,
    }
