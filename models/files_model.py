from pydantic import BaseModel
from datetime import date, datetime, time, timedelta


class File(BaseModel):
    id: int = None
    file: str = None
    user_id: str = None
    created_at: datetime = None
    updated_at: datetime = None
