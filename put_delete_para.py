from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, computed_field, Field
from typing import Annotated, Literal, Optional
import json
import os

app = FastAPI()

# -------------------- Models --------------------

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
        return round((self.weight / (self.height ** 2)), 2)


class UpdatePatient(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = Field(default=None, gt=0)
    gender: Optional[Literal["male", "female", "other"]] = None
    height: Optional[float] = Field(default=None, gt=0)
    weight: Optional[float] = Field(default=None, gt=0)


# -------------------- Helper Functions --------------------

def load_data():
    if not os.path.exists("patients.json"):
        return {}
    with open("patients.json", "r") as f:
        return json.load(f)


def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)


# -------------------- Routes --------------------

@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, update_patient: UpdatePatient):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Existing patient data
    existing_patient_info = data[patient_id]

    # Get only provided fields
    updated_patient_info = update_patient.model_dump(exclude_unset=True)

    # Update fields
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    # Add id back (required for Patient model)
    existing_patient_info["id"] = patient_id

    # Recalculate BMI using Pydantic model
    patient_obj = Patient(**existing_patient_info)

    # Convert back to dict (exclude id if you don't want to store it)
    updated_data = patient_obj.model_dump(exclude={"id"})

    # Save updated data
    data[patient_id] = updated_data

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient updated successfully",
            "data": data[patient_id]
        }
    )

# delete endpoint
print ("==================================================")
@app.delete("/delete/{patient_id}")
def delete(patient_id:str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code = 404, details= "patient not found.")
    del data[patient_id]
    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient deleted successfully",
            
        })