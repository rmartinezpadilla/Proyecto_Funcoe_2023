"""
Entidad Usuarios
"""
from pydantic import BaseModel
import datetime

class User(BaseModel):
    cedula : int
    first_name : str
    last_name : str
    rol : str
    user_name : str
    password : str
    created_at : datetime    
    last_conection : datetime
    update_at : datetime
    