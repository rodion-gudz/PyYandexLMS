from datetime import datetime
from typing import List, Optional, Union

from PyYandexLMS.models.base import BaseModel, BaseSolution
from PyYandexLMS.models.lesson import BaseLesson


class Tag(BaseModel):
    id: int
    type: str
    color: str
    order: int


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


class TaskType(BaseModel):
    id: int
    type: str
    color: str
    order: int
    tasks: List[BaseTask]


class File(BaseModel):
    id: int
    name: str
    url: str
    mime_type: str
    encoding: str
    size: int
    run_id: str
    added_time: datetime


class Submission(BaseModel):
    id: int
    file: File
    contest_id: int
    problem_id: str
    run_id: str
    compiler_id: str
    got_verdict_time: Union[datetime, None]
    verdict: str
    is_rejudgement_of_id: Union[int, None]


class Variant(BaseModel):
    id: int
    index: int


class Task(BaseTask):
    variant: Variant
    description: str
    compilers_ids: List[int]
    solution_id: int
    latest_submission: Union[Submission, None]
