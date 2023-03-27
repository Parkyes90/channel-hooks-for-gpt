from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    print()
    return {"Hello": "World"}


class Event(BaseModel):
    event: str
    type: str
    entity: dict
    referer: dict | None


@app.post("/webhook")
async def webhook(token: str, event: Event):
    print(token, event)
    return {
        "test": "test"
    }
