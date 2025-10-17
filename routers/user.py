from fastapi import APIRouter
import json
import schema
from database import initialize_db
from llm import model
router = APIRouter(tags=["users"])
db=initialize_db("RecSys_Cloud")
chatHistory=db.chatHistory
@router.post("/recommendations")
def get_recommendations(request: schema.Input):
    results = model.recommendation(request.query)

    info={
        "user":request.query,
        "recommendations":results["result"]
    }

    chatHistory.insert_one(info)
    return {"results": results["result"]}

@router.post("/searchBook")
def search_book(request: schema.SearchInput):
    results = model.search_books_by_kwords(keyword=request.query, genre=request.genre)
    return {"results": results}


