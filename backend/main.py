from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Card(BaseModel):
    id: int
    name: str
    age: int
    bio: str

FAKE_CARDS = [
    {"id": 1, "name": "Alice", "age": 25, "bio": "Loves hiking and coffee."},
    {"id": 2, "name": "Bob", "age": 30, "bio": "Adventurous and fun."},
]

@app.get("/cards", response_model=list[Card])
async def get_cards():
    return FAKE_CARDS
