from pydantic import BaseModel
from typing import Optional


class LogTask(BaseModel):
    status: str


class LogProducer(BaseModel):
    correlation_id: str
    queue_name: str
    service_name: str
    task_type: str
    description: Optional[str] = None


class LogReceiver(BaseModel):
    correlation_id: str
    queue_name: str
    service_name: str
    task_type: str
    description: Optional[str] = None


class LogWorkflow(BaseModel):
    service_id: str
    queue_name: str
