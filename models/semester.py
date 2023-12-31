"""
Entidad semestre
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Semester(BaseModel):
    semester_name : str
    createt_at : datetime
    update_at : Optional[datetime] = None