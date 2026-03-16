from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Student(BaseModel):
    #Anotated purpose: With the help of Field we can do custom data validation,meta data and give default values.
    name: str = Annotated[str,Field(max_length=20,title="Name of the student.",description="Give the name of the student in less then 20 characters.")]
    email:EmailStr
    linkedin:AnyUrl
    age: int = Field(gt=0,lt=100)
    address : Optional[str]=None
    total_student_name:List[str]
    contact_details:Dict[str,int]
    weight:Annotated[float,Field(gt=0,strict=True)]

def student_info(student: Student):
    print(student.name)
    print(student.email)
    print(student.linkedin)
    print(student.age)
    print(student.address)
    print(student.contact_details)
    print(student.total_student_name)
    print(student.weight)
student1 = {"name": "Muhammad Faraz",
            "email": "abc@gmail.com",
            "linkedin":"https://linkedin.com/5582",
            "age":25,
            "address":"chak no.97Rb johal.",
            "contact_details":{"Ayan": 6734,"Hammad":8907,"Hassam":4329,"Anas":7766},
            "total_student_name":["Ali","Faraz","Husnain","Ahmad","Ubaid","Junaid"],
            "weight":67.7
            }
obj1 = Student(**student1)
student_info(obj1)