from fastapi import APIRouter

# add from here: 
# https://fastapi.tiangolo.com/tutorial/bigger-applications/
router = APIRouter()

@router.get("/", tags=["main page"])
async def home():
    return {"message": "this is our home page."}