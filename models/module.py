""" 
Entidad modulos
"""

from pydantic import BaseModel

class Modules(BaseModel):
    module_name : str
    program_id : str
    semester_id : str