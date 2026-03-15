from fastapi import FastAPI,Path,HTTPException
import json
app = FastAPI()

def load():
    with open('patients.json','r') as file:
          data=json.load(file)
    return data

@app.get("/patients/{patient_id}")
def patient_id(patient_id:str=Path(...,description="id of the patient in the DB",example="P001")):
    #load all the patients.
    load_data= load()
    if patient_id in load_data:
          return load_data[patient_id]
    raise HTTPException(status_code=404,detail = "patient not found.")      