from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    # id: Optional[str]
    name: str
    surname: str
    age: int
    height: Optional[float]
