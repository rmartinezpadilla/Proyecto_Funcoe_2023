"""
entidad conceptos

"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Document_type(BaseModel):
    document_name : str
    create_at : datetime
    update_at : Optional[datetime] = None