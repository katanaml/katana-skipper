from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dataservice.app.api.service import dataservice

app = FastAPI(openapi_url='/api/v1/data/openapi.json', docs_url='/api/v1/data/docs')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(dataservice, prefix='/api/v1/data')