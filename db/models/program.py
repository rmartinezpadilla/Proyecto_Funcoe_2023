"""
Entidad programas
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Programs(BaseModel):
    id : Optional[str] = None
    program_name : str
    created_at : datetime
    update_at : datetime = None