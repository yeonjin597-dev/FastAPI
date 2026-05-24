from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

DATA_FILE = "courses.json"


class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str


def read_courses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def write_courses(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@app.get("/courses")
def get_courses():
    return read_courses()


@app.post("/courses")
def add_course(course: Course):
    data = read_courses()
    data.append(course.model_dump())
    write_courses(data)
    return course
