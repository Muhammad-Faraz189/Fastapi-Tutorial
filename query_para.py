from fastapi import FastAPI, Query, HTTPException
import json

app = FastAPI()

def load():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(..., description="Sort by height, weight, bmi"),
    order: str = Query(..., description="Sort in asc or desc order")
):

    valid_fields = ["height","weight","bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid field. Select from {valid_fields}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Select between asc and desc"
        )

    data = load()

    sort_order = True if order == "desc" else False

    sorted_data = sorted(
        data["patients"],
        key=lambda x: x.get(sort_by, ""),
        reverse=sort_order
    )

    return sorted_data