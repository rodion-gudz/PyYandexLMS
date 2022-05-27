from datetime import date, datetime, time
from typing import List, Optional, Union

from PyYandexLMS.models.base import BaseModel


class Group(BaseModel):
    id: int
    name: str


class SchedulePlanItem(BaseModel):
    id: int
    schedule_plan: int
    day_of_week: int
    start_time: time


class SchedulePlan(BaseModel):
    id: int
    group: int
    study_period: int
    start_date: date
    items: List[SchedulePlanItem]


class Progress(BaseModel):
    num_tasks: Optional[int]
    num_passed: Optional[int]
    num_rework: Optional[int]


class Invite(BaseModel):
    url: str
    uses_count: int
    uses_limit: int


class BaseUser(BaseModel):
    id: int
    uid: int
    username: str
    last_name: str
    first_name: str
    middle_name: str
    display_name: str
    avatar: str
    gender: str


class Placement(BaseModel):
    venue: Union[str, None]
    city: Union[str, None]


class Course(BaseModel):
    id: int
    title: str
    teacher: Union[BaseUser, None]
    teachers_list: Union[List[BaseUser], None]
    group: Group
    rating: float
    bonus_score: float
    progress: Progress
    use_bonus_score: bool
    max_bonus_score: float
    certificate_id: Union[int, None]
    pass_type: str
    certificate_number: Union[str, None]
    logo: Union[str, None]
    logo_height: Union[int, None]
    logo_width: Union[int, None]
    is_archive: bool
    is_active: bool
    status: str
    events_count: int
    visited_attendances_count: int
    schedule_plan: SchedulePlan


class CoursesSummary(BaseModel):
    student: Union[List[Course], None]
    teacher: Union[List[BaseUser], None]


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


class User(BaseModel):
    profile: Profile
    courses_summary: Union[CoursesSummary, None]
    placement: Placement
