from datetime import datetime
from typing import Union, Optional

from PyYandexLMS.models.base import BaseModel


class BaseLesson(BaseModel):
    id: int
    short_title: str
    title: str
    type: str
    num_tasks: int
    num_passed: int
    deadline: datetime
    ms_before_deadline: Optional[int]
    has_assigned_variant: bool


class Lesson(BaseLesson):
    description: str
    duration: Union[int, None]
    score: int
    is_test_started: Union[bool, None]
    is_test_finished: Union[bool, None]
    manual_variants_assignment: bool
