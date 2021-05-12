from pydantic import BaseModel
from enum import Enum
from typing import Optional


class TaskType(str, Enum):
    TRAINING = 'training'
    INFERENCE = 'inference'


class WorkflowTaskData(BaseModel):
    task_type: TaskType
    payload: str
    description: Optional[str] = None


class WorkflowTask(BaseModel):
    task_id: str
    task_status: str


class WorkflowTaskResult(BaseModel):
    task_id: str
    task_status: str
    outcome: str
