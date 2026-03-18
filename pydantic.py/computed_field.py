from pydantic import BaseModel,computed_field
from typing import List,Dict

class Student(BaseModel):
    name: str
    age: int
    address: str
    weight:float
    height : float
    total_student_name:List[str]
    contact_details:Dict[str,int]

#computed Field
    @computed_field()
    @property
    def calculate_bmi(self)->float:
        bmi = round((self.weight/self.height**2),2)  #for round-off upto 2 decimal.
        return bmi

    



def student_info(student: Student):
    print(student.name)
    print(student.age)
    print(student.address)
    print(student.weight)
    print(student.height)
    print(student.contact_details)
    print("BMI:",student.calculate_bmi)
    print("student info")
    




s1 = {"name":"Faraz","age":25,"address":"Chak no 97 RB Johal Faisalabad","weight":67.7,"height":5.8,"total_student_name":["Ayan","Ali","Misbah"],"contact_details":{"Ayan":5463,"Ali":9807,"Misbah":3421}}  
obj =Student(**s1)  

# obj = Student(name="Faraz", age=25, address="Chak no 97 RB Johal Faisalabad") #we can also write like that.

student_info(obj)

