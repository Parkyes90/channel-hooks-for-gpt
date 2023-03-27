from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

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
    headers = {"x-quick-reply": "true", "x-bot-name": "GREPP_GPT"}
    return JSONResponse(content={
        "blocks": [
            {
                "type": "text",
                "value": "This is <b>bold</b>, <i>italic</i>, and <b><i>bold+italic</i></b>. Emoji should be in shortcode :+1: :100: "
            },
            {
                "type": "text",
                "value": "<link type=\"manager\" value=\"managerId_goes_here\">@username</link>"
            },
            {
                "type": "text",
                "value": "This is a url <link type=\"url\" value=\"https://channel.io\">https://channel.io</link>"
            },
            {
                "type": "text",
                "value": "This is a link <link type=\"url\" value=\"https://channel.io\">Channel</link>"
            },
            {
                "type": "code",
                "value": "<script>ChannelIO('boot')</script>"
            },
            {
                "type": "bullets",
                "blocks": [
                    {
                        "type": "text",
                        "value": "Bulleted text goes here"
                    },
                    {
                        "type": "text",
                        "value": "Next bulleted text goes here"
                    }
                ]
            }
        ]
    }, headers=headers)
