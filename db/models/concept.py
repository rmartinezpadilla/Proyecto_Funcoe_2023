"""
entidad conceptos

"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Concepts(BaseModel):
    id : Optional[str] = None
    concept_name : str
    create_at : datetime
    update_at : datetime = None