from pydantic import BaseModel
from datetime import date, datetime, time, timedelta


class User(BaseModel):
    id: int = None
    name: str = None
    cv: str = None
    lastName: str = None
    surName: str = None
    rfc: str = None
    birthday: datetime = None
    profilePicture: str = None
    created_at: datetime = None
    updated_at: datetime = None

