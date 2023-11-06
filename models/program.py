"""
Entidad programas
"""

from pydantic import BaseModel
import datetime

class Programs(BaseModel):
    program_name : str
    created_at : datetime
    update_at : datetime