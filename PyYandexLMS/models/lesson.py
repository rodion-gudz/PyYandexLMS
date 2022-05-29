from typing import Union

from PyYandexLMS.models.base import BaseLesson


class Lesson(BaseLesson):
    description: str
    duration: Union[int, None]
    score: int
    is_test_started: Union[bool, None]
    is_test_finished: Union[bool, None]
