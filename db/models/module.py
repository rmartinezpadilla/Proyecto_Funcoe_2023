""" 
Entidad modulos
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Modules(BaseModel):
    id : Optional[str] = None
    module_name : str
    program_id : str
    semester_id : str
    created_at : datetime
    update_at : Optional[datetime] = None