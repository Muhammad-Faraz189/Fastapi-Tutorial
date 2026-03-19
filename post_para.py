from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, computed_field,Field
from typing import Annotated, Literal
import json
import os

app = FastAPI()

class Patient(BaseModel):
    id: str
    name: Annotated[str, Field(..., description="Name of the patient", example="Ali Khan")]
    age: Annotated[int, Field(..., gt=0, lt=120)]
    gender: Annotated[Literal["male", "female", "other"], Field(...)]
    email: EmailStr
    weight: Annotated[float, Field(..., gt=0)]
    height: Annotated[float, Field(..., gt=0)]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        return round((self.weight / self.height ** 2), 2)


# Load data
def load_data():
    if not os.path.exists("patients.json"):
        return {}
    with open("patients.json", "r") as f:
        return json.load(f)


# Save data
def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)


# POST Endpoint
@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()

    # Check if patient exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    # Add new patient
    data[patient.id] = patient.model_dump(exclude=["id"])

    save_data(data)

    return JSONResponse(
        status_code=201,
        content={"message": "Patient created successfully"}
    )