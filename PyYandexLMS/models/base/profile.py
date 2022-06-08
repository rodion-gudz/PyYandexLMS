from datetime import date, datetime
from typing import List, Union, Dict

from PyYandexLMS.models.user import User


class BaseProfile(User):
    timezone: str
    phone: str
    email: str
    birth_date: Union[date, None]
    date_joined: datetime
    is_staff: bool
    is_superuser: bool
    is_editable: bool
    tags: List[str]
    city: str
    clubs: str
    competitions: str
    parents_info: Union[List[str], Dict]
    programming_experience: str
    school: str
    school_class: str
    children: Union[List[int]]
    parents: Union[List[int]]
