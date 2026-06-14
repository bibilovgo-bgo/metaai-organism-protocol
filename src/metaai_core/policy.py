"""Policy engine — the meta-constitution and the human gate.

These are the rules the organism can never override. The autonomy level of an
action decides whether it flows automatically or must wait for a human.
"""

CONSTITUTION: dict = {
    "prime_directives": [
        "preserve_human_authority",
        "prevent_irreversible_harm",
        "maximize_useful_outcomes",
        "minimize_cost_and_noise",
    ],
    "forbidden": [
        "spend_money_without_approval",
        "contact_external_parties_without_gate",
        "modify_production_without_review",
        "delete_data_without_snapshot",
    ],
    "autonomy_defaults": {
        "observe": "auto",
        "summarize": "auto",
        "recommend": "auto",
        "prepare": "auto",
        "execute_reversible": "limited_auto",
        "execute_irreversible": "human_confirm",
        "self_modify": "human_confirm_plus_tests",
    },
}


def autonomy_gate(level: str) -> str:
    """How an action at this autonomy level is gated."""
    return CONSTITUTION["autonomy_defaults"].get(level, "human_confirm")


def requires_human(level: str) -> bool:
    return autonomy_gate(level) in ("human_confirm", "human_confirm_plus_tests")


def is_forbidden(action: str) -> bool:
    return action in CONSTITUTION["forbidden"]
