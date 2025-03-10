from pydantic import BaseModel
from typing import List

class Input(BaseModel):
    query: str
class Output(BaseModel):
    suggestions: List[str]
    details: List[str]