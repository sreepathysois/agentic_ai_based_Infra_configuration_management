from app.graph.llm import llm

def intent_agent(state):
    prompt = f"""
Classify the intent into one word:
install | configure | audit | harden | rollback

Request:
{state['user_request']}
"""
    state["intent"] = llm.invoke(prompt).content.strip().lower()
    return state
