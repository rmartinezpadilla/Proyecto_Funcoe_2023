"""
Entidad Docente
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Teacher(BaseModel):
    id : Optional[str] = None
    document_type_id : str
    identification_card : int
    birth_date : datetime
    first_name : str
    last_name : str    
    address : str
    phone : int    
    user_name : str
    password : str
    last_conection : datetime
    program_id : str
    created_at : datetime    
    update_at : Optional[datetime] = None
    