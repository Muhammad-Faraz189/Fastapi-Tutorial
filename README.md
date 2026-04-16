FastAPI 

> A structured collection of FastAPI implementations covering core API development concepts with clean and practical examples.

---

About This Project:

This repository demonstrates how to build modern APIs using FastAPI with a strong focus on:

* Clean routing
* Request handling
* Data validation using Pydantic
* RESTful API design principles

It is created as a **learning + reference project** for developers who want to understand FastAPI in depth.

---

What’s Implemented:

Routing & HTTP Methods

* GET → Fetch data
* POST → Create new records
* PUT → Update existing data
* DELETE → Remove data

---

Parameters Handling:

Path Parameters:

Used for dynamic routing:

```python
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

Query Parameters:

Used for filtering and optional inputs:

```python
@app.get("/items/")
def get_items(limit: int = 10):
    return {"limit": limit}
```

---

Pydantic Models (Data Validation):

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_available: bool = True
```

✔ Automatic validation
✔ Type checking
✔ Clean request body handling

---

Folder Layout:

```
fastapi-project/
│
├── main.py
├── models/
├── routers/
├── schemas/
└── utils/
```



Run Server:

```bash
uvicorn main:app --reload
```

API Base URL:
http://127.0.0.1:8000

---

Auto API Docs

FastAPI gives built-in docs:

* Swagger → `/docs`
* ReDoc → `/redoc`

---

Example Endpoints:

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| GET    | /items      | Get all items   |
| GET    | /items/{id} | Get single item |
| POST   | /items      | Create item     |
| PUT    | /items/{id} | Update item     |
| DELETE | /items/{id} | Delete item     |

---

Purpose:

This project is built to:

* Practice FastAPI fundamentals
* Understand request/response cycle
* Learn API structuring
* Improve backend development skills

---

Next Steps:

* Add database (SQLAlchemy)
* Authentication system
* File uploads
* Deployment (Docker / Cloud)

---


 Developer
 Muhammad Faraz
 <br>

---


