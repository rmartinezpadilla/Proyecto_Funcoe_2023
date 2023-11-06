"""
entidad días de la semana

"""
from pydantic import BaseModel
import datetime

class Days(BaseModel):
    day_name : str
    create_at : datetime
    update_at : datetime