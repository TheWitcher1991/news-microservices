from pydantic import BaseModel, Field


class PostCreateSchema(BaseModel):

    title: str = Field(min_length=1, max_length=255, examples=["Complete the project"])
    description: str | None = Field(
        default=None,
        max_length=3000,
        examples=["Finish implementing the DDD architecture"],
    )
