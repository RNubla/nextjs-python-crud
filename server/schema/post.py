from pydantic import BaseModel


class PostSchema(BaseModel):
    Title: str
    Body: str
