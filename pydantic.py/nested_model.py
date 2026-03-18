#use one model into another model as a field is known as nested model.
from pydantic import BaseModel


class Address(BaseModel):
    city : str
    state : str
    pincode : int

class Student(BaseModel):
    name :str
    age :int
    gender:str
    address : Address

#Address object
address_dict = {                 
    "city":"Faisalabad",
    "state": "Punjab",
    "pincode":882244
}
s1 = Address(**address_dict)

#Student object
student_dict = {
    "name":"Faraz",
    "age": 25,
    "gender":"Male",
    "address":s1
}

s2 =Student(**student_dict)
 
print(s2) 
print(s2.address.pincode)
print(s2.address.city)
print(s2.address.state)