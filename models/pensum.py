"""
entindad Pensum
"""
from pydantic import BaseModel
import datetime

class Pensum(BaseModel):
    program_id : str
    semester_id : str
    number_of_classes : int
    value : float
    created_at: datetime
    