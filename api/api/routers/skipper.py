from fastapi import APIRouter

router = APIRouter()


@router.get('/', tags=['skipper'])
def skipper():
    return 'Skipper API is running'
