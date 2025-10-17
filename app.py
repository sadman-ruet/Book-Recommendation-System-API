from fastapi import FastAPI
from llm import model
import os
from routers import user
from fastapi.responses import FileResponse
app = FastAPI()
app.include_router(user.router)
@app.get("/")
def index():
    # return {"message": "FastAPI running on HF Spaces!"}
    file_path = os.path.join(os.path.dirname(__file__), "FrontEnd", "index.html")
    return FileResponse(file_path)
