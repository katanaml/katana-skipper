from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import router_workflow

# docs available at 
# http://127.0.0.1:5000/docs
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(router_workflow, prefix='/api/v1/skipper/workflow')
