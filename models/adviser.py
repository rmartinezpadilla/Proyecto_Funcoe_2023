"""
entidad asesor

"""
from pydantic import BaseModel
import datetime


class Adviser(BaseModel):
    identification_card : int
    first_name : str
    last_name : str
    phone : int
    create_at : datetime
    update_at:  datetime
    


