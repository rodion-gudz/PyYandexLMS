from typing import Union

from PyYandexLMS.models.base.lesson import BaseLesson
from PyYandexLMS.models.base.main import BaseModel


class Lesson(BaseLesson):
    description: str
    duration: Union[int, None]
    score: int
    is_test_started: Union[bool, None]
    is_test_finished: Union[bool, None]


class NotificationLesson(BaseModel):
    id: int
    type: str
    title: str
    is_accepted: bool
    short_title: str
