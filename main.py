from model import ml_pipeline 

from typing import Union
from fastapi import FastAPI


## Note: FastAPI default provides http://127.0.0.1:8000/docs url to access "Swagger UI" API/Endpoints Documentation.


# app means creating a FastAPI instance/object
app = FastAPI()



@app.get("/")
def read_root():
    return {"ML recommendation model deployment using": "FastAPI"}



@app.post("/recommendations")
def request_recommendations(movie: str, rating: int):
    # pass

    recommendations = ml_pipeline(movie, rating)

    return recommendations
    
    # return {"similar movies": recommendations}
