from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Student(BaseModel):
    name: str
    age: int
    email:EmailStr
    address: str
    total_student_name:List[str]
    contact_details:Dict[str,int]

    #if we want specific fix name
    #Field validator
    @field_validator("email")
    @classmethod
    def email_validator(cls,value):
        valid_domains = ["hbl.com","ubldigital.com"]
        #abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain.")
        return value
    
    #if we want student name in capital letter.
    @field_validator("name")
    @classmethod
    def transform_name(cls,value):
        return value.upper()


        
def student_info(student: Student):
    print(student.name)
    print(student.age)
    print(student.email)
    print(student.address)
    print(student.contact_details)

s1 = {"name":"Faraz","age":25,"address":"Chak no 97 RB Johal Faisalabad","email":"abc@hbl.com","total_student_name":["Ayan","Ali","Misbah"],"contact_details":{"Ayan":5463,"Ali":9807,"Misbah":3421}}  
obj =Student(**s1)
student_info(obj)     