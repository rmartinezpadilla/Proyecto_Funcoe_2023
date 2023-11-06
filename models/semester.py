"""
Entidad semestre
"""
from pydantic import BaseModel
from datetime import datetime

class Semester(BaseModel):
    semester_name : str
    createt_at : datetime
    update_at : datetime