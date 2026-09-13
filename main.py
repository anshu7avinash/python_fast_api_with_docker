from fastapi import FastAPI, HTTPException, status


#OOP: we create real world object
#BankAccount: Saving/Current account
from pydantic import BaseModel, EmailStr, Field


app = FastAPI(title="Student Management API")


students_dict = {}
student_counter = 1


#using class we can create object....class is a blueprint
class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)  
    email:  EmailStr
    branch: str = Field(min_length=3, max_length=20)
    year: int = Field(ge=2000, le=2026)


class StudentUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    branch: str = Field(min_length=3, max_length=20)
    year: int = Field(ge=2000, le=2026)


class StudentPatch(BaseModel):
    name: str | None = Field(default=None,min_length=2, max_length=100)
    email: EmailStr | None = None
    branch: str | None = Field(default=None,min_length=3, max_length=20)
    year: int | None = Field(default=None,ge=2000, le=2026)


@app.post("/students", status_code = status.HTTP_201_CREATED)
def create_student(student: StudentCreate):
    global student_counter


    student_id = student_counter


    students_dict[student_id] = {
        "id" : student_id,
        "name" : student.name,
        "email" : student.email,
        "branch" : student.branch,
        "year" : student.year
    }


    student_counter +=1
    print(student_counter)
    return students_dict[student_id]


@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentUpdate):
    if student_id not in students_dict:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )


    students_dict[student_id]= {
        "id": student_id,
        "name": student.name,
        "email": student.email,
        "branch": student.branch,
        "year": student.year
    }


    return students_dict[student_id]


@app.get("/students")
def get_students():
    return {
        "data": list(students_dict.values()),
        "total": len(students_dict)
    }


@app.patch("/students/{student_id}")
def patch_student(student_id: int, student: StudentPatch):
    if student_id not in students_dict:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    update_data = student.model_dump(exclude_unset = True)


    #Data we got from frontend = {"branch" : "ECE"}
    #{"name": None, "email: None, "branch": "ECE", "year": None}


    students_dict[student_id].update(update_data)


    return students_dict[student_id]




@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    if student_id not in students_dict:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )


    del students_dict[student_id]
    return None
