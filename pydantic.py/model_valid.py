from pydantic import BaseModel,model_validator
from typing import List,Dict

class Student(BaseModel):
    name: str
    age: int
    address: str
    weight:float
    height : float
    total_student_name:List[str]
    contact_details:Dict[str,int]

    #Model validator
    @model_validator(mode="after")
    def emergency_contact(cls,model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Student older than 60 must have emergency contact.")
        return model



def student_info(student: Student):
    print(student.name)
    print(student.age)
    print(student.address)
    print(student.weight)
    print(student.height)
    print(student.contact_details)
    print("student info")
    




s1 = {"name":"Faraz","age":68,"address":"Chak no 97 RB Johal Faisalabad","weight":67.7,"height":5.8,"total_student_name":["Ayan","Ali","Misbah"],"contact_details":{"Ayan":5463,"Ali":9807,"Misbah":3421,"emergency":555111}}  
obj =Student(**s1)  

# obj = Student(name="Faraz", age=25, address="Chak no 97 RB Johal Faisalabad") #we can also write like that.

student_info(obj)

