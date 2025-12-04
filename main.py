from fastapi import FastAPI
import uvicorn
from todorouters import router

app = FastAPI()

app.include_router(router, tags=["Todo methods"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
