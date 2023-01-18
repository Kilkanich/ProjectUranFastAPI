from pydantic import BaseModel
from datetime import date

class Comics(BaseModel):
    title: str
    present: str
    duration: int
    date: date
    summary: str
    genres: str = None
