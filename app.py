from fastapi import FastAPI, Header,status
import uvicorn

app = FastAPI()

@app.get("/test")
async def test_app():
    return {"message": "Welcome To FastAPI World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


