"""
entidad días de la semana

"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Days(BaseModel):
    id : Optional[str] = None
    day_name : str
    create_at : datetime
    update_at : datetime = None