from pydantic import BaseModel


class Post(BaseModel):
    """Post data model."""

    post_url: str
    image_url: str
    title: str
    address: str
    price: str
    size: str
    rooms: str
