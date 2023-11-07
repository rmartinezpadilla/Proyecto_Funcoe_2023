""" 
Entidad Pagos
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Payments(BaseModel):
    id : Optional[str] = None
    enroll_id : str
    concept_id : str
    value : float
    pyament_date : datetime
    created_at : datetime
    update_at : Optional[datetime] = None