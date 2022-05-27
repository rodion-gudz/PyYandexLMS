from datetime import datetime
from typing import Union, Optional, List

from PyYandexLMS.models.base import BaseModel
from PyYandexLMS.models.lesson import BaseLesson


class Status(BaseModel):
    id: int
    type: str


class Solution(BaseModel):
    id: int
    score: int
    status: Status
    task_id: int
    added_time: datetime
    update_time: datetime


class Tag(BaseModel):
    id: int
    type: str
    color: str
    order: int


class Task(BaseModel):
    id: int
    short_title: str
    title: str
    tag: Tag
    score_max: int
    lesson: BaseLesson
    solution: Solution
    deadline: datetime
    is_contest_integrated: bool
    has_manual_check: bool


class TaskType(BaseModel):
    id: int
    type: str
    color: str
    order: int
    tasks: List[Task]
