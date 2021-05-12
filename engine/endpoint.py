from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.router import router_tasks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(router_tasks, prefix='/api/v1/skipper/tasks')
