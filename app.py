from fastapi import FastAPI, Depends,status,HTTPException
import schemas
import uvicorn
from config import *
import auth

app = FastAPI()

@app.get("/test")
async def test_app():
    return {"message": "Welcome To FastAPI World"}

@app.post("/users/auth", response_model=schemas.Token, tags=["users"])
async def authenticate_user(user: schemas.UserAuthenticate):
    db_user = True if data["user"]["email"] == user.username else None
    if db_user is None:
        raise HTTPException(status_code=403, detail="Username or password is incorrect")
    else:
        is_password_correct = auth.check_username_password(data, user)
        if is_password_correct is False:
            raise HTTPException(status_code=403, detail="Username or password is incorrect")
        else:
            from datetime import timedelta
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = auth.encode_jwt_token(
                data={"sub": user.username}, expires_delta=access_token_expires)
            return {"access_token": access_token, "token_type": "Bearer"}
        

@app.get("/posts",dependencies=[Depends(auth.verify_token)],response_model= schemas.PostResponse)
async def post_list():
    post = data["post"]
    if post:
        return {"data": post, "count": len(post)}
    else:
        raise HTTPException(status_code=404, detail="Note not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


