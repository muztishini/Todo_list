from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Hello!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
    