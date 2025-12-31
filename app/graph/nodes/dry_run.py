import subprocess
import uuid
import os

PLAYBOOK_DIR = "app/ansible/playbooks"

def dry_run_agent(state):
    os.makedirs(PLAYBOOK_DIR, exist_ok=True)

    become_pass = os.getenv("ANSIBLE_BECOME_PASS")
    if not become_pass:
        raise RuntimeError(
            "ANSIBLE_BECOME_PASS is not set. "
            "Export it before running the app."
        )

    playbook_id = str(uuid.uuid4())
    playbook_path = f"{PLAYBOOK_DIR}/generated_{playbook_id}.yml"

    with open(playbook_path, "w") as f:
        f.write(state["playbook_yaml"])

    env = os.environ.copy()
    env["ANSIBLE_BECOME_PASS"] = become_pass

    proc = subprocess.run(
        ["ansible-playbook", playbook_path, "--check"],
        capture_output=True,
        text=True,
        env=env
    )

    state["dry_run_output"] = proc.stdout + proc.stderr
    state["approved"] = proc.returncode == 0
    state["playbook_path"] = playbook_path
    state["playbook_id"] = playbook_id

    return state

