from pydantic import BaseModel
from pydantic import create_model
from enum import Enum
from typing import Optional


class TaskType(str, Enum):
    TRAINING = 'training'
    SERVING = 'serving'
    MOBILENET = 'mobilenet'


class WorkflowTaskDataTraining(BaseModel):
    task_type: TaskType = TaskType.TRAINING
    payload: str
    description: Optional[str] = None


class WorkflowTaskDataPredict(BaseModel):
    task_type: TaskType = TaskType.SERVING
    payload: str
    data: Optional[create_model('Data',
                                crim=(float, ...),
                                zn=(int, ...),
                                indus=(float, ...),
                                chas=(int, ...),
                                nox=(float, ...),
                                rm=(float, ...),
                                age=(float, ...),
                                dis=(float, ...),
                                rad=(int, ...),
                                tax=(int, ...),
                                b=(float, ...),
                                lstat=4.98)] = None
    description: Optional[str] = None


class WorkflowTaskDataMobileNet(BaseModel):
    task_type: TaskType = TaskType.MOBILENET
    payload: str
    data: Optional[create_model('DataMobileNet',
                                image='orange.jpeg')] = None
    description: Optional[str] = None


class WorkflowTask(BaseModel):
    task_id: str
    task_status: str


class WorkflowTaskResult(BaseModel):
    task_id: str
    task_status: str
    outcome: str


class WorkflowTaskCancelled(BaseModel):
    task_id: str
    task_status: str
