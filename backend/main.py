from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import all_routers


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# app.include_router(all_routers.home.router, prefix='/api/v1/')
