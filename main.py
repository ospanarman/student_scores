from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Student Endpoints
@app.post("/students/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db=db, student=student)

@app.get("/students/{student_id}", response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.patch("/students/{student_id}", response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = crud.update_student(db, student_id=student_id, student=student)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.delete("/students/{student_id}", response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.delete_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

#Score Endpoints
@app.post("/scores/", response_model=schemas.Score)
def create_score(score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    return crud.create_score(db=db, score=score)

@app.get("/scores/{score_id}", response_model=schemas.Score)
def read_score(score_id: int, db: Session = Depends(get_db)):
    db_score = crud.get_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score

@app.patch("/scores/{score_id}", response_model=schemas.Score)
def update_score(score_id: int, score: schemas.ScoreCreate, db: Session = Depends(get_db)):
    db_score = crud.update_score(db, score_id=score_id, score=score)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score

@app.delete("/scores/{score_id}", response_model=schemas.Score)
def delete_score(score_id: int, db: Session = Depends(get_db)):
    db_score = crud.delete_score(db, score_id=score_id)
    if db_score is None:
        raise HTTPException(status_code=404, detail="Score not found")
    return db_score