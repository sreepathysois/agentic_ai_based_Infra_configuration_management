from typing import TypedDict, List, Dict, Optional

class InfraState(TypedDict):
    user_request: str
    intent: Optional[str]
    plan: Optional[Dict]
    playbook_yaml: Optional[str]
    playbook_path: Optional[str]
    playbook_id: Optional[str]
    validation_errors: List[str]
    dry_run_output: Optional[str]
    execution_output: Optional[str]
    verification_output: Optional[Dict]
    approved: bool
    status: str

