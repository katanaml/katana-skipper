from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import skipper, boston, mobilenet
import os

app = FastAPI(openapi_url="/api/v1/skipper/tasks/openapi.json",
              docs_url="/api/v1/skipper/tasks/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

boston_enabled = os.getenv('BOSTON_ENABLED', 'y')
mobilenet_enabled = os.getenv('MOBILENET_ENABLED', 'y')

app.include_router(skipper.router, prefix='/api/v1/skipper/tasks')
if boston_enabled == 'y':
    app.include_router(boston.router, prefix='/api/v1/skipper/tasks')
if mobilenet_enabled == 'y':
    app.include_router(mobilenet.router, prefix='/api/v1/skipper/tasks')
