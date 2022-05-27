from datetime import datetime

from PyYandexLMS.models.base import BaseModel


class BaseLesson(BaseModel):
    id: int
    short_title: str
    title: str
    type: str
    num_tasks: int
    num_passed: int
    deadline: datetime
    ms_before_deadline: int
    has_assigned_variant: bool
