"""
entidad asesor

"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Adviser(BaseModel):
    id : Optional[str] = None
    document_type : str
    identification_card : int
    first_name : str
    last_name : str
    phone : int
    create_at : datetime
    update_at:  Optional[datetime] = None
    


