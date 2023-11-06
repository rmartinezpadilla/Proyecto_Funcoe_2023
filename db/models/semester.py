"""
Entidad semestre
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Semester(BaseModel):
    id : Optional[str] = None
    semester_name : str
    createt_at : datetime
    update_at : Optional[datetime] = None