import json

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from api import get_image, predict
from setup_lifespan import lifespan

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,  # https://fastapi.tiangolo.com/tutorial/cors/
    allow_origins=[
        "*"
    ],  # wildcard to allow all, more here - https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin
    allow_credentials=True,  # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials
    allow_methods=[
        "*"
    ],  # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Methods
    allow_headers=[
        "*"
    ],  # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Headers
)


# Base root
@app.get("/")
async def get_hello_page():
    return {"msg": "hello from blur service"}


@app.post("/predict")
async def post_detect(request: Request):
    retries = 3
    try:
        model = request.app.state.model
        db_cursor = request.app.state.db_cursor
        response = await request.json()
        if isinstance(response, str):
            while retries >= 0:
                # Normally, it executes 2 times and break.
                response = json.loads(response)
                # print(type(payload))
                if type(response) == dict:
                    break
                retries -= 1

        image_body = response.get("image")
        blur_list = response.get("blur_list")
        if not isinstance(image_body, str):
            raise TypeError(f"Invalid input")
        image = get_image(image_body)
        response = predict(
            model=model, img_obj=image, cursor=db_cursor, blur_list=blur_list
        )
        return response

    except Exception as e:
        raise e
