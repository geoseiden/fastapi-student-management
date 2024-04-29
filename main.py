from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import func
from database import SessionLocal
from models import *
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Add the origin of your AngularJS app
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#================================================================
# Schemas
#================================================================

class MentorSchema(BaseModel):
    empid: str  
    name: str
    desig: str  
    email: str
    ph: int  

class MentorCreateSchema(MentorSchema):
    password: str

class StudentSchema(BaseModel):
    regno: str
    name: str
    email: str
    phone: int
    programme: str
    score: int
    empid: str

#================================================================
# Mentor CRUD
#================================================================

@app.get("/mentors", response_model=List[MentorSchema])
def get_mentors(db: Session = Depends(get_db)):
    mentors = db.query(Mentors).with_entities(Mentors.empid, Mentors.name, Mentors.desig, Mentors.email, Mentors.ph).all()
    return [{"empid": empid, "name": name, "desig": desig, "email": email, "ph": ph} for empid, name, desig, email, ph in mentors]

@app.get("/mentors/{empid}", response_model=MentorSchema)
def get_mentor_by_empid(empid: int, db: Session = Depends(get_db)):
    mentor = db.query(Mentors).filter(Mentors.empid == empid).first()
    if not mentor:
        raise HTTPException(status_code=404, detail="Mentor Not Found")
    return mentor

@app.post("/mentors", response_model=MentorSchema)
def create_mentor(user: MentorCreateSchema, db: Session = Depends(get_db)):
    u = Mentors(empid=user.empid,name=user.name, desig=user.desig, email=user.email, ph=user.ph, password=user.password)
    db.add(u)  
    db.commit()  
    db.refresh(u)  
    return u

@app.put("/mentors/{empid}", response_model=MentorSchema)
def update_mentor(empid: int, mentor: MentorSchema, db: Session = Depends(get_db)):
    existing_mentor = db.query(Mentors).filter(Mentors.empid == empid).first()
    if not existing_mentor:
        raise HTTPException(status_code=404, detail=f"Mentor with empid {empid} not found")
    for field, value in mentor.dict().items():
        setattr(existing_mentor, field, value)
    db.commit()
    return existing_mentor


@app.delete("/mentors/{empid}")
def delete_user(empid: int, db: Session = Depends(get_db)):
    u = db.query(Mentors).filter(Mentors.empid == empid).first()
    if not u:
        raise HTTPException(status_code=404, detail="User Not Found")

    db.delete(u)
    db.commit()

    return {"message": f"User with ID {empid} has been deleted"}

# Students CRUD

@app.get("/students", response_model=List[StudentSchema])
def get_students(db: Session = Depends(get_db)):
    return db.query(Students).all()

@app.get("/students/{regno}", response_model=StudentSchema)
def get_student_by_regno(regno: str, db: Session = Depends(get_db)):
    student = db.query(Students).filter(Students.regno == regno).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student Not Found")
    return student

@app.post("/students", response_model=StudentSchema)
def create_student(student: StudentSchema, db: Session = Depends(get_db)):
    s = Students(**student.dict())
    db.add(s)
    db.commit()
    db.refresh(s)
    return s

@app.put("/students/{regno}", response_model=StudentSchema)
def update_student(regno: str, student: StudentSchema, db: Session = Depends(get_db)):
    s = db.query(Students).filter(Students.regno == regno).first()
    if not s:
        raise HTTPException(status_code=404, detail="Student Not Found")

    for field, value in student.dict().items():
        setattr(s, field, value)

    db.commit()
    db.refresh(s)

    return s

@app.delete("/students/{regno}")
def delete_student(regno: str, db: Session = Depends(get_db)):
    s = db.query(Students).filter(Students.regno == regno).first()
    if not s:
        raise HTTPException(status_code=404, detail="Student Not Found")

    db.delete(s)
    db.commit()

    return {"message": f"Student with Registration Number {regno} has been deleted"}

@app.get("/students/mentor/{empid}", response_model=List[StudentSchema])
def get_students_by_mentor(empid: str, db: Session = Depends(get_db)):
    students = db.query(Students).filter(Students.empid == empid).all()
    if not students:
        raise HTTPException(status_code=404, detail=f"No students found for mentor with empid {empid}")
    return students
