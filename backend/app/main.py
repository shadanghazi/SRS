import json
from fastapi import FastAPI, HTTPException, status
from models import StudentCreate,StudentOut,StudentUpdate
from storage import load_students,save_students

app=FastAPI(
    title="SRS",
    description="Student currently Studying",
    version="1.0"
)

@app.get("/")
def home():
    return {"app": "SRS", "message":"Students currently studying"}

@app.get("/students", response_model=list[StudentOut])
def list_students():
    return load_students()

@app.get("/student/{student_id}", response_model=StudentOut)
def get_student(student_id:int):
    for student in load_students():
        if student["id"]==student_id:
            return student
    raise HTTPException(status_code= 404, detail=f"{student_id} not found")

@app.post("/students", status_code=status.HTTP_201_CREATED, response_model=StudentOut)
def create_student(student: StudentCreate):
    students = load_students()
    new_id= max((s["id"] for s in students), default=0)+1
    new_student= {"id": new_id, **student.model_dump()}
    students.append(new_student)
    save_students(students)
    return new_student

@app.put("/students{student_id}", response_model=StudentOut)
def update_student(student_id: int, student:StudentUpdate):
    students=load_students()
    for i,s in enumerate(students):
        if s["id"]== student_id:
            students[i]= {"id": student_id, **student.model_dump()}
            save_students(students)
            return student[i]
    raise HTTPException(status_code=404, detail=f"{student_id} not found")

@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    students = load_students()
    remaining = [s for s in students if s["id"]!=student_id]
    if len(remaining)==len(students):
        raise HTTPException(status_code=404, detail=f"{student_id} not found")
    save_students(remaining)
    



