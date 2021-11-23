from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import skipper, boston, mobilenet

app = FastAPI(openapi_url="/api/v1/skipper/tasks/openapi.json",
              docs_url="/api/v1/skipper/tasks/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(skipper.router, prefix='/api/v1/skipper/tasks')
app.include_router(boston.router, prefix='/api/v1/skipper/tasks')
app.include_router(mobilenet.router, prefix='/api/v1/skipper/tasks')
