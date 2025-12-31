import subprocess
import os

def executor_agent(state):
    if not state.get("approved"):
        state["status"] = "ABORTED"
        return state

    become_pass = os.getenv("ANSIBLE_BECOME_PASS")
    if not become_pass:
        raise RuntimeError(
            "ANSIBLE_BECOME_PASS is not set. "
            "Export it before running the app."
        )

    env = os.environ.copy()
    env["ANSIBLE_BECOME_PASS"] = become_pass

    proc = subprocess.run(
        ["ansible-playbook", state["playbook_path"]],
        capture_output=True,
        text=True,
        env=env
    )

    state["execution_output"] = proc.stdout + proc.stderr
    state["status"] = "EXECUTED"

    return state

