def policy_validator(state):
    errors = []
    pb = state["playbook_yaml"]

    forbidden = [
        "```",
        "Here is",
        "shell:",
        "command:",
        "idempotent:"
    ]

    for f in forbidden:
        if f in pb:
            errors.append(f"Forbidden content detected: {f}")

    if "hosts:" not in pb:
        errors.append("Missing hosts")

    if "become: true" not in pb:
        errors.append("Missing become: true")

    state["validation_errors"] = errors
    return state

