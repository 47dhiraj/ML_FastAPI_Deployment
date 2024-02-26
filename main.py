from model import ml_recommendation_model 

from typing import Union
from fastapi import FastAPI


## Note: FastAPI default provides http://127.0.0.1:8000/docs url to access "Swagger UI" API/Endpoints Documentation.


# creating a FastAPI instance/object
app = FastAPI()



@app.get("/")
def read_root():
    return {"ML recommendation model deployment using": "FastAPI"}



@app.post("/recommendations")
def request_recommendations(movie: str, rating: int):

    recommendations = ml_recommendation_model(movie, rating)

    # return recommendations
    return {"similar movies": recommendations}
