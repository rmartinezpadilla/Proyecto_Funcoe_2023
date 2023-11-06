""" 
Entidad Pagos
"""

from pydantic import BaseModel
import datetime

class Payments(BaseModel):
    enroll_id : str
    concept_id : str
    value : float
    pyament_date : datetime
    created_at : datetime
    update_at : datetime