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

#model_dump() return us a dictionary.
temp_dict = s2.model_dump()
#if we want only specific field name like name
temp_dict = s2.model_dump(include=['name'])

#if we want data in json form
json= s2.model_dump_json()

print(temp_dict)
print(type(temp_dict))

print(json)
print(type(json))