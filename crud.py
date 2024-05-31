from sqlalchemy.orm import Session
import models, schemas

# CRUD Student
def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def update_student(db: Session, student_id: int, student: schemas.StudentCreate):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        db_student.name = student.name
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student

# CRUD Score
def get_score(db: Session, score_id: int):
    return db.query(models.Score).filter(models.Score.id == score_id).first()

def create_score(db: Session, score: schemas.ScoreCreate):
    db_score = models.Score(score=score.score, student_id=score.student_id)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def update_score(db: Session, score_id: int, score: schemas.ScoreCreate):
    db_score = db.query(models.Score).filter(models.Score.id == score_id).first()
    if db_score:
        db_score.score = score.score
        db_score.student_id = score.student_id
        db.commit()
        db.refresh(db_score)
    return db_score

def delete_score(db: Session, score_id: int):
    db_score = db.query(models.Score).filter(models.Score.id == score_id).first()
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score
