from fastapi import FastAPI
from starlette import status
from starlette.middleware.cors import CORSMiddleware

from src.presentation.routes import NewsRouter

app = FastAPI(
    openapi_version="3.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
    redoc_url="/redoc/",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/is-health/")
async def health_check():
    return status.HTTP_200_OK


app.include_router(NewsRouter().include_routers())
