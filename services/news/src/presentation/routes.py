from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from services.news.src.application.usecases.create_post import CreatePostUseCase
from services.news.src.interface.dependencies import get_create_post_use_case
from services.news.src.presentation.schemas import PostCreateSchema
from services.shared.kernel.result import Result


class NewsRouter:
    def __init__(self):
        self.router = APIRouter(tags=["News"], prefix="/news")
        self.include_routers()

    def include_routers(self):
        self.create_post_route()

    def create_post_route(self):
        @self.router.post("/")
        async def create_post(data: PostCreateSchema, use_case: CreatePostUseCase = Depends(get_create_post_use_case)):
            try:
                post = use_case.execute(data.title, data.description)
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Result.success(post)
