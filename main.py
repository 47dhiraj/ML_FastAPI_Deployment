from model import ml_pipeline 

from typing import Union

from fastapi import FastAPI



app = FastAPI()


@app.get("/")
def read_root():
    return {"me": "47"}

