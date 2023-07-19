from pydantic import BaseModel
from datetime import date, datetime, time, timedelta


class File(BaseModel):
    id: int
    file: str
    user_id: str
    created_at: datetime
    updated_at: datetime
