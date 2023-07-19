from pydantic import BaseModel
from datetime import date, datetime, time, timedelta


class User(BaseModel):
    id: int
    name: str
    id_1: int
    lastName: str
    surName: str
    rfc: str
    birthday: datetime
    profilePicture: str
    created_at: datetime
    updated_at: datetime
