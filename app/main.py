from fastapi import FastAPI
from config.settings import settings
from routers import human_query_router

app = FastAPI()

app.include_router(human_query_router.router)
