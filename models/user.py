"""
Entidad Usuarios
"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    cedula : int
    first_name : str
    last_name : str
    rol : str
    user_name : str
    password : str
    created_at : datetime    
    last_conection : datetime
    update_at : Optional[datetime] = None
    