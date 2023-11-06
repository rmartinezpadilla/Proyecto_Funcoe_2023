"""
entidad conceptos

"""
from pydantic import BaseModel
from datetime import datetime

class Concepts(BaseModel):
    concept_name : str
    create_at : datetime
    update_at : datetime = None