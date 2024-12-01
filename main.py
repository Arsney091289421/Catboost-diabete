from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import cloudpickle

# Load the saved pipeline
with open("pipeline_catboost.pkl", "rb") as f:
    pipeline = cloudpickle.load(f)

# Initialize FastAPI app
app = FastAPI()

# Define the input schema
class InputData(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

# Prediction endpoint
@app.post("/predict")
def predict(input_data: InputData):
    # Convert input to a Pandas DataFrame
    input_df = pd.DataFrame([input_data.dict()])
    
    # Predict class and probabilities
    prediction = pipeline.predict(input_df)
    probabilities = pipeline.predict_proba(input_df)
    
    # Map prediction to human-readable labels
    prediction_label = "Diabetes" if prediction[0] == 1 else "No Diabetes"
    
    # Return the result
    return {
        "prediction": prediction_label,
        "probability": {
             "No Diabetes (Class 0)": f"{probabilities[0][0] * 100:.2f}%",  # percent
        "Diabetes (Class 1)": f"{probabilities[0][1] * 100:.2f}%"
        }
    }

# Health check endpoint
@app.get("/")
def health_check():
    return {"status": "API is running"}
