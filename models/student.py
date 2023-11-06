"""
Entidad estudiante
"""

from pydantic import BaseModel
import datetime


class Estudent(BaseModel):
    identification_card : int
    birth_date = datetime
    first_name : str
    last_name : str
    municipality : str
    address : str
    phone : int
    gender : str
    recommendation : str
    #medio publicitario
    advertising_medium : str
    day_id : str
    created_at : datetime
    #jornada
    working_day : str
    register_number : int
    adviser_id : str
    