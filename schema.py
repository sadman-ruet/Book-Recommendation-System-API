from pydantic import BaseModel
from typing import List,Optional

class Input(BaseModel):
    query: str
class Output(BaseModel):
    suggestions: List[str]
    details: List[str]

class SearchInput(BaseModel):
    query: str
    genre: Optional[str] = None