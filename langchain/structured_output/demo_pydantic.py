from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
  name: str = 'luffy'
  age: Optional[int] = None
  email: EmailStr
  cgpa: float = Field(gt=0, lt=10, default=5, description="cgpa of student")


new_student = {'age': 20, 'email': "abc@xyz.com"}

student = Student(**new_student)

student_dict = student.model_dump()

print(student_dict)
print(type(student_dict))

