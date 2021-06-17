from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import router_workflow

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(router_workflow, prefix='/api/v1/skipper/workflow')
