"""
entidad asesor

"""

import datetime
import uuid
#from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime
from db.connection_to_MySQL import Base

class Adviserdb(Base):
    __tablename__ = 'asesores'    
    uuid = Column(String, primary_key=True, index=True, default=uuid.uuid4, unique=True)
    id_document_type = Column(String(200), index=True)
    identification_card = Column(Integer, unique=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone = Column(String(20))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    update_at= Column(DateTime, default=datetime.datetime.utcnow)