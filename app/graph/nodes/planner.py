import json
import re
from app.graph.llm import llm

def extract_json(text: str):
    """
    Extract first JSON object found in text
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in LLM output")
    return match.group(0)

def planner_agent(state):
    prompt = f"""
You are an infrastructure planner.

Return ONLY valid JSON.
Do NOT add explanations.
Do NOT use markdown.
Do NOT add text before or after JSON.

JSON schema:
{{
  "os": "ubuntu",
  "inventory_group": "web",
  "tasks": [
    {{
      "name": "Install nginx",
      "package": "nginx",
      "state": "present"
    }}
  ]
}}

User request:
{state["user_request"]}
"""

    raw = llm.invoke(prompt).content.strip()

    try:
        json_text = extract_json(raw)
        state["plan"] = json.loads(json_text)
    except Exception as e:
        state["plan"] = None
        state["status"] = f"PLAN_PARSE_ERROR: {str(e)}"
        raise

    return state

