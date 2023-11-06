"""
Entidad programas
"""

from pydantic import BaseModel
from datetime import datetime

class Programs(BaseModel):
    program_name : str
    created_at : datetime
    update_at : datetime = None