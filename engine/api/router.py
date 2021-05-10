from fastapi import APIRouter
from .models import WorkflowTask

router = APIRouter()


@router.get('/')
def touch():
    return 'API is running'
