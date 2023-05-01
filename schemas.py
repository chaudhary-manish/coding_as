from pydantic import BaseModel
from typing import List

class UserAuthenticate(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class Post(BaseModel):
    user_id:int
    post_id:int
    category_id:int
    post_name:str
    post_title:str
    post_description:str
   
class PostResponse(BaseModel):
    data:List[Post]
    count:int

