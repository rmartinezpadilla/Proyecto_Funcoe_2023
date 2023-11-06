""" 
Entidad modulos
"""

from pydantic import BaseModel
from datetime import datetime

class Modules(BaseModel):
    module_name : str
    program_id : str
    semester_id : str
    created_at : datetime
    update_at : datetime = None