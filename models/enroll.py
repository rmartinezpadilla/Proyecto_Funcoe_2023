"""
entidad matricula

"""
from pydantic import BaseModel
from typing import Optional
import datetime

class Enroll(BaseModel):
    student_id : str
    progam_id : str
    semester_id : str
    value : float
    pending_to_pay : float
    positive_balance : float
    quotas : int
    quota_number : int
    pay_for_quota : float
    create_at : datetime
    update_at : datetime