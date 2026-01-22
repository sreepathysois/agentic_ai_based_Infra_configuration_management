# 🧠 Infra AI Agent

Agentic Infrastructure Automation using LangGraph, FastAPI, Ansible & Ollama

## 📌 Project Overview

Infra AI Agent is an agentic AI–driven infrastructure automation platform that allows users to manage servers using natural language queries.

Instead of manually writing Ansible playbooks, users can simply ask:

```bash
“Install nginx on all Ubuntu web servers”
“Uninstall nginx from all web servers”
“Install nginx and deploy a sample website”
```
The system uses LLM-powered agents orchestrated via LangGraph to:

* Understand intent

* Plan infrastructure changes

* Generate Ansible playbooks

* Perform dry-run validation

* Execute changes safely

* Verify results

This project demonstrates how Agentic AI can act as a control plane for infrastructure operations.

## 🎯 Objectives

**The primary objectives of this project are:**

✅ Build a multi-agent AI system using LangGraph

✅ Convert natural language → infrastructure actions

✅ Enforce safe execution using dry-run & approval flow

✅ Automate infrastructure using Ansible (SSH-based)

✅ Provide a web-based UI for interaction

✅ Support local, Docker, and lab-network execution

## 🧩 High-Level Architecture
```bash
User (Browser / UI)
        |
        v
React Frontend (Vite)
        |
        v
FastAPI Backend (8085)
        |
        v
LangGraph (Agent Orchestration)
        |
        v
Ollama LLM (llama3)
        |
        v
Ansible (SSH)
        |
        v
Ubuntu Inventory Hosts
```

## 🛠️ Technologies & Frameworks Used
### 🔹 Backend

* Python 3.12

* FastAPI – REST API backend

* LangGraph – Agent orchestration & state machine

* LangChain – LLM abstraction

* Ollama – Self-hosted LLM runtime (llama3)

* Ansible – Infrastructure execution engine

* SSH – Secure remote access

### 🔹 Frontend

* React

* Vite

* Axios – API communication

### 🔹 Infrastructure

* Ubuntu servers (lab nodes)

* SSH key-based authentication

* Optional Docker support

## 📁 Repository Structure
```bash
infra-ai-agent/
├── app/
│   ├── main.py                 # FastAPI entrypoint
│   ├── graph/
│   │   ├── graph.py             # LangGraph definition
│   │   ├── state.py             # Shared state schema
│   │   └── nodes/
│   │       ├── intent.py        # Intent agent
│   │       ├── planner.py       # Planning agent
│   │       ├── generator.py     # Playbook generator
│   │       ├── validator.py     # YAML validation
│   │       ├── dry_run.py       # Ansible dry-run
│   │       ├── executor.py      # Ansible execution
│   │       └── verifier.py      # Post-execution verification
│   └── ansible/
│       ├── inventory.ini        # Inventory hosts
│       ├── ansible.cfg          # Ansible configuration
│       └── playbooks/
│           └── generated_*.yml  # Generated playbooks
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx              # UI logic
│   │   └── api.js               # Axios client
│   └── vite.config.js
│
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
└── README.md
```

## 🤖 Agent Design & Responsibilities (LangGraph)

**This project follows a true agentic architecture.** 

### 🟦 1. Intent Agent
```bash
Purpose:
Understands what the user wants.

Input:
Natural language query

Output:

"install" | "uninstall" | "configure"
```

### 🟦 2. Planner Agent
```bash
Purpose:
Converts intent into a structured execution plan.

Example Output:

{
  "os": "ubuntu",
  "inventory_group": "web",
  "tasks": [
    { "package": "nginx", "state": "present" }
  ]
}
```

### 🟦 3. Playbook Generator Agent
```bash
Purpose:
Generates a valid Ansible YAML playbook from the plan.

Adds become: true

Handles ansible_check_mode

Applies best practices
```

### 🟦 4. Validator Agent
```bash
Purpose:
Validates YAML syntax and Ansible structure.

Prevents invalid playbooks

No infrastructure access
```

### 🟦 5. Dry-Run Agent
```bash
Purpose:
Runs:

ansible-playbook --check --diff


Simulates changes

Detects errors early

Skips unsafe tasks (copy, shell, git)
```

### 🟦 6. Approval Agent
```bash
Purpose:
Decides whether execution should proceed.

Currently auto-approved

Designed for future UI-based human approval
```

### 🟦 7. Execution Agent
```bash
Purpose:
Applies changes for real using Ansible.

This is the only agent allowed to modify infrastructure.
```

### 🟦 8. Verification Agent
```bash
Purpose:
Confirms that the desired state is achieved.

Example:

Is nginx installed?

Is service running?
```

### 🔄 Execution Flow
```bash
User Query
   ↓
Intent Agent
   ↓
Planner Agent
   ↓
Playbook Generator
   ↓
Validator
   ↓
Dry-Run (Ansible --check)
   ↓
Approval
   ↓
Execution (Ansible)
   ↓
Verification
```

## ▶️ Running the Project (Without Docker)
### 1️⃣ Start Ollama
```bash 
ollama run llama3


Ensure API is accessible:

curl http://localhost:11434/v1/chat/completions
```

### 2️⃣ Backend (FastAPI)
```bash
cd infra-ai-agent
source venv/bin/activate

export ANSIBLE_BECOME_PASS=university
export OLLAMA_BASE_URL=http://localhost:11434/v1

uvicorn app.main:app --host 0.0.0.0 --port 8085 --reload


Test:

http://<IP>:8085/docs
```

### 3️⃣ Frontend (React)
```bash 
cd frontend
npm install
npm run dev -- --host


Access UI:

http://<IP>:5173
```

### 🧪 Example Queries
```bash
Install nginx

Install nginx on all ubuntu web servers


Uninstall nginx

Uninstall nginx on all ubuntu web servers
```

### ✅ Sample Output (UI / API)
```bash
{
  "intent": "install",
  "plan": {...},
  "dry_run_output": "No errors",
  "execution_output": "changed=1",
  "approved": true,
  "status": "VERIFIED"
}
```
## 🔐 Security Considerations

* SSH key-based authentication

* No hardcoded credentials

* sudo password via environment variable

* Designed to support container-generated SSH identities

## 🚀 Future Enhancements

* UI-based approval / reject flow

* Execution history & audit logs

* Rollback agent

* Role-based access control (RBAC)

* Kubernetes deployment

* Secrets manager integration

## 🏁 Conclusion

Infra AI Agent demonstrates how Agentic AI + Infrastructure Automation can be combined to create a safe, extensible, and production-style automation platform.

**This project highlights:**

* Modern AI orchestration (LangGraph)

* Infrastructure best practices

* Secure execution models

* Real-world DevOps/SRE workflows
