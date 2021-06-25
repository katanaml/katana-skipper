from pydantic import BaseModel, Json


class LogTask(BaseModel):
    status: str


class LogProducer(BaseModel):
    correlation_id: str
    queue_name: str
    service_name: str
    task_type: str


class LogReceiver(BaseModel):
    correlation_id: str
    queue_name: str
    service_name: str
    task_type: str


class LogWorkflow(BaseModel):
    service_id: str
    queue_name: str
