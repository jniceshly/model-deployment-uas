from fastapi import FastAPI
from input import Input
from prediction import predict_bank_subscription

# TO RUN APP
# In the directory of this file run this command
# "uvicorn api:app --reload"

app = FastAPI()

@app.get("/")
async def information() :
    return "go to '/docs' to try the API"

@app.post("/predict")
async def read_root(input: Input):
    return predict_bank_subscription(input)