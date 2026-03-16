from pydantic import BaseModel
from typing import List,Dict

class Student(BaseModel):
    name: str
    age: int
    address: str
    weight:float
    total_student_name:List[str]
    contact_details:Dict[str,int]


def student_info(student: Student):
    print(student.name)
    print(student.age)
    print(student.address)
    print(student.contact_details)
    print("student info")
    print("===========================================")

def update_student_data(student:Student):
    print(student.name)
    print(student.age)
    print(student.address)
    print(student.weight)
    print("update student data")


s1 = {"name":"Faraz","age":25,"address":"Chak no 97 RB Johal Faisalabad","weight":67.7,"total_student_name":["Ayan","Ali","Misbah"],"contact_details":{"Ayan":5463,"Ali":9807,"Misbah":3421}}  
obj =Student(**s1)  

# obj = Student(name="Faraz", age=25, address="Chak no 97 RB Johal Faisalabad") #we can also write like that.

student_info(obj)
update_student_data(obj)
