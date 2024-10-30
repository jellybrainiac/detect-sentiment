import json

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware    

from setup_lifespan import lifespan

from api import get_image, predict

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
@app.get('/')
async def get_hello_page(): 
    return {'msg': "helloword"}


@app.post('/detect')
async def post_detect(request: Request):
    retries = 3
    try: 
        model = request.app.state.model
        print(1)
        response = await request.json()

        if isinstance(response, str):
            while retries >= 0:
                # Normally, it executes 2 times and break.
                response = json.loads(response)
                # print(type(payload))
                if type(response) == dict:
                    break
                retries -= 1
        image_body = response.get('image')
        if not isinstance(image_body, str): 
            raise TypeError(f"Invalid input")
        print(1)
        image = get_image(image_body)
        print(1)

        response = predict(model, img_obj=image)
        return response
    
    except Exception as e: 
        raise e