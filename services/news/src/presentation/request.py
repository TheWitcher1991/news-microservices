from typing import Optional

from pydantic import BaseModel, Field

from services.news.src.domain.enums import PostStatus


class WritablePostRequest(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(max_length=3000)
    status: Optional[PostStatus] = Field(..., description="Статус поста: draft или published")
