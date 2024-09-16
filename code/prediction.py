import pickle
import pandas as pd
from input import Input
    
with open('../model/random_forest_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)
    
print("Random Forest Model Loaded")    

def predict_bank_subscription(input: Input):
    inputs = pd.DataFrame([{
        'age': input.age,
        'job': input.job,
        'marital': input.marital,
        'education': input.education,
        'default': input.default,
        'housing': input.housing,
        'loan': input.loan,
        'contact': input.contact,
        'month': input.month,
        'day_of_week': input.day_of_week,
        'duration': input.duration,
        'campaign': input.campaign,
        'pdays': input.pdays,
        'previous': input.previous,
        'poutcome': input.poutcome
    }])

    prediction = rf_model.predict(inputs)
    
    if prediction[0] == 0:
        return "Will Not Subscribe"
    else :
        return "Will Subscribe"
