from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}

class RequestItem(BaseModel):
    name: str

@app.post("/post/")
def post_request(req: RequestItem):
    return {"req": req.name,}

#DRIVE REQUESTS
    
@app.post("/post/drive/forwards")
def post_drive_forwards():
    return {"req": "drive_forwards"}

@app.post("/post/drive/backwards")
def post_drive_backwards():
    return {"req": "drive_backwards",}

@app.post("/post/drive/turnleft")
def post_drive_turnleft():
    return {"req": "drive_turnleft",}

@app.post("/post/drive/turnright")
def post_drive_turnright():
    return {"req": "drive_turnright",}
