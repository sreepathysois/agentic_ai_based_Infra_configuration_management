import subprocess

def verify_agent(state):
    checks = {
        "nginx": "systemctl is-active nginx"
    }

    result = {}
    for k, cmd in checks.items():
        p = subprocess.run(cmd.split(), capture_output=True)
        result[k] = p.returncode == 0

    state["verification_output"] = result
    state["status"] = "VERIFIED"
    return state

