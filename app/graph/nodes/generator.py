import re
from app.graph.llm import llm

def extract_yaml(text: str) -> str:
    text = re.sub(r"```yaml", "", text, flags=re.IGNORECASE)
    text = re.sub(r"```", "", text)

    lines = text.strip().splitlines()
    yaml_start = None

    for i, line in enumerate(lines):
        if line.strip().startswith("---") or line.strip().startswith("- hosts"):
            yaml_start = i
            break

    if yaml_start is None:
        raise ValueError("No YAML found")

    return "\n".join(lines[yaml_start:]).strip()


def playbook_generator(state):
    prompt = f"""
You are an Ansible playbook generator.

Return ONLY valid Ansible YAML.
DO NOT explain.
DO NOT use markdown.
DO NOT invent attributes.

IMPORTANT:
- DO NOT use 'idempotent' as a YAML field.
- Idempotency must come from using proper Ansible modules.

Rules:
- hosts: {state["plan"]["inventory_group"]}
- become: true
- use apt and service modules only
- no shell or command

Plan:
{state["plan"]}
"""

    raw = llm.invoke(prompt).content.strip()
    state["playbook_yaml"] = extract_yaml(raw)
    return state

