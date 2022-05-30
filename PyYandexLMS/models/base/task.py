from datetime import datetime
from typing import Optional, Union

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.lesson import BaseLesson
from PyYandexLMS.models.solution import BaseSolution
from PyYandexLMS.models.tag import Tag


class BaseTask(BaseModel):
    id: int
    short_title: str
    title: str
    tag: Tag
    score_max: int
    lesson: BaseLesson
    solution: Optional[BaseSolution]
    deadline: Union[datetime, None]
    is_contest_integrated: bool
    has_manual_check: bool
