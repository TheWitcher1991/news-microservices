from fastapi import APIRouter, Depends, HTTPException
from services.news.src.application.usecases.create_post import CreatePostUseCase
from services.news.src.application.usecases.delete_post import DeletePostUseCase
from services.news.src.application.usecases.find_post import FindPostUseCase
from services.news.src.application.usecases.find_posts import FindPostsUseCase
from services.news.src.application.usecases.update_post import UpdatePostUseCase
from services.news.src.application.validators.create_post import CreatePostValidator
from services.news.src.application.validators.update_post import UpdatePostValidator
from services.news.src.domain.value_objects import PostId
from services.news.src.interface.dependencies import (
    get_create_post_use_case,
    get_create_post_validator,
    get_delete_post_use_case,
    get_find_post_use_case,
    get_find_posts_use_case,
    get_update_post_use_case,
    get_update_post_validator,
)
from services.news.src.presentation.request import WritablePostRequest
from services.shared.cases.exceptions import InternalErrorResult
from services.shared.kernel.result import Result
from starlette import status


class NewsRouter:
    def __init__(self):
        self.router = APIRouter(tags=["news"], prefix="/news")
        self.include_routers()

    def include_routers(self):
        self.create_post_route()
        self.update_post_route()
        self.delete_post_route()
        self.find_post_route()
        self.find_posts_route()

    def create_post_route(self):
        @self.router.post("/")
        async def create_post(
            data: WritablePostRequest,
            validator: CreatePostValidator = Depends(get_create_post_validator),
            use_case: CreatePostUseCase = Depends(get_create_post_use_case),
        ):
            result = validator.validate(data)

            if not result.is_valid:
                return Result.failure(result.to_list())

            try:
                post = use_case.execute(data.title, data.description)
            except Exception as e:
                return InternalErrorResult()

            return Result.success(post)

    def update_post_route(self):
        @self.router.put("/{id}")
        async def create_post(
            id: PostId,
            data: WritablePostRequest,
            validator: UpdatePostValidator = Depends(get_update_post_validator),
            use_case: UpdatePostUseCase = Depends(get_update_post_use_case),
        ):
            result = validator.validate(data)

            if not result.is_valid:
                return Result.failure(result.to_list())

            try:
                post = use_case.execute(id, data.title, data.description, data.status)
            except Exception as e:
                return InternalErrorResult()

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
                return InternalErrorResult()

            return Result.success(post)

    def find_posts_route(self):
        @self.router.get("/")
        async def find_post(use_case: FindPostsUseCase = Depends(get_find_posts_use_case)):
            try:
                post = use_case.execute()
            except Exception as e:
                return InternalErrorResult()

            return Result.success(post)
