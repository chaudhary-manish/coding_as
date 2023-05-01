from pydantic import BaseModel
from typing import List

class UserAuthenticate(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


