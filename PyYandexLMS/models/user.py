from datetime import date, datetime
from typing import List, Union

from PyYandexLMS.models.base import BaseModel, BaseUser, Group
from PyYandexLMS.models.course import CoursesSummary


class Invite(BaseModel):
    url: str
    uses_count: int
    uses_limit: int


class Placement(BaseModel):
    venue: Union[str, None]
    city: Union[str, None]


class BaseProfile(BaseUser):
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
    parents_info: List[str]
    programming_experience: str
    school: str
    school_class: str
    children: Union[List[int]]
    parents: Union[List[int]]


class Profile(BaseProfile):
    children: Union[List[BaseProfile], None]
    parents: Union[List[BaseProfile], None]
    groups: List[Group]
    permissions: List[str]
    managed_cities: List[str]
    managed_venues: List[str]
    city_to_managed_venues: List[str]
    invite: Invite


class UserInformation(BaseModel):
    profile: Profile
    courses_summary: Union[CoursesSummary, None]
    placement: Placement
