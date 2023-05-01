import datetime
import bcrypt
import jwt
import schemas
import time
from typing import Annotated
from fastapi import Header
from config import *


def verify_token(token: Annotated[str, Header()]): 
    try:   
        token = token.split(" ")[1]
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except:
        raise credentials_exception
    
def check_username_password(data: data, user: schemas.UserAuthenticate):
    if data["user"]["email"] == user.username:    
        db_pass = data["user"]["password"].encode('utf8')
        request_pass = user.password.encode('utf8')
        return bcrypt.checkpw(request_pass, db_pass)

def encode_jwt_token(*, data: dict, expires_delta: datetime.timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt
