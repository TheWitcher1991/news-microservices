from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from services.news.src.application.usecases.create_post import CreatePostUseCase
from services.news.src.application.usecases.delete_post import DeletePostUseCase
from services.news.src.application.usecases.find_post import FindPostUseCase
from services.news.src.application.usecases.find_posts import FindPostsUseCase
from services.news.src.domain.value_objects import PostId
from services.news.src.interface.dependencies import get_create_post_use_case, get_find_post_use_case, \
    get_find_posts_use_case, get_delete_post_use_case
from services.news.src.presentation.request import WritablePostRequest
from services.shared.kernel.result import Result


class NewsRouter:
    def __init__(self):
        self.router = APIRouter(tags=["news"], prefix="/news")
        self.include_routers()

    def include_routers(self):
        self.create_post_route()
        self.delete_post_route()
        self.find_post_route()
        self.find_posts_route()

    def create_post_route(self):
        @self.router.post("/")
        async def create_post(data: WritablePostRequest,
                              use_case: CreatePostUseCase = Depends(get_create_post_use_case)):
            try:
                post = use_case.execute(data.title, data.description)
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Result.success(post)

    def delete_post_route(self):
        @self.router.delete("/{id}")
        async def find_post(id: PostId, use_case: DeletePostUseCase = Depends(get_delete_post_use_case)):
            try:
                post = use_case.execute(id)
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Result.success(post)

    def find_post_route(self):
        @self.router.get("/{id}")
        async def find_post(id: PostId, use_case: FindPostUseCase = Depends(get_find_post_use_case)):
            try:
                post = use_case.execute(id)
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Result.success(post)

    def find_posts_route(self):
        @self.router.get("/")
        async def find_post(use_case: FindPostsUseCase = Depends(get_find_posts_use_case)):
            try:
                post = use_case.execute()
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Result.success(post)
