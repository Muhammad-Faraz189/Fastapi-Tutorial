from fastapi import FastAPI
import json
app = FastAPI()

def load():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data    


@app.get("/")
def name():
    return {"message": "Ptient managment system API."}

@app.get("/about")   #endpoint
def about():
    return{"message":"Fully functional API to manage your patient records."}

@app.get("/view")
def view():
    data = load()
    return data

