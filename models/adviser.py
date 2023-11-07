"""
entidad asesor

"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Adviser(BaseModel):
    document_type : str
    identification_card : int
    first_name : str
    last_name : str
    phone : int
    created_at : datetime
    updated_at:  Optional[datetime] = None
    


