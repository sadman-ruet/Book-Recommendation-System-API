from fastapi import FastAPI
from llm import model
from routers import user
app = FastAPI()
app.include_router(user.router)
@app.get("/")
def index():
    return {"message": "Hello World"}