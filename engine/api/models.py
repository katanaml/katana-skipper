from pydantic import BaseModel


class WorkflowTask(BaseModel):
    taskId: str
    taskResult: str
