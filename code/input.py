from pydantic import BaseModel

class Input(BaseModel):
    age: int
    job: int
    marital: int
    education: int
    default: int
    housing: int
    loan: int
    contact: int
    month: int
    day_of_week: int
    duration: float
    campaign: int
    pdays: int
    previous: int
    poutcome: int