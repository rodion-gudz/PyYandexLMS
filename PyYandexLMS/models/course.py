from typing import List, Optional, Union

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.group import Group
from PyYandexLMS.models.progress import Progress
from PyYandexLMS.models.schedule_plan import SchedulePlan
from PyYandexLMS.models.user import User


class Course(BaseModel):
    id: int
    title: str
    teacher: Union[User, None]
    teachers_list: Union[List[User], None]
    group: Group
    rating: Optional[float]
    bonus_score: Optional[float]
    progress: Optional[Progress]
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
    status: Optional[str]
    events_count: Optional[int]
    visited_attendances_count: Optional[int]
    schedule_plan: SchedulePlan


class CoursesSummary(BaseModel):
    student: Union[List[Course], None]
    teacher: Union[List[Course], None]
