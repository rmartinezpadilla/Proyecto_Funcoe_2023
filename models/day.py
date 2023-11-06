"""
entidad días de la semana

"""
from pydantic import BaseModel
from datetime import datetime

class Days(BaseModel):
    day_name : str
    create_at : datetime
    update_at : datetime = None