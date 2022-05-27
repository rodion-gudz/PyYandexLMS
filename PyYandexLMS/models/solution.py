from datetime import datetime
from typing import Union, Optional, List

from PyYandexLMS.models.base import BaseModel
from PyYandexLMS.models.task import Status, File, Submission, Task, BaseTask
from PyYandexLMS.models.user import BaseUser


class VerdictOfSubmission(BaseModel):
    id: int
    contest_score: float
    file: File
    contest_id: int
    problem_id: str
    run_id: int
    compiler_id: str
    got_verdict_time: datetime
    verdict: str
    compile_log: str
    used_time: Union[int, None]
    used_memory: Union[int, None]
    test_number: Union[int, None]
    is_rejudgement_of_id: Union[bool, None]


class Comment(BaseModel):
    id: int
    author: BaseUser
    type: str
    data: str
    files: List[File]
    is_changed: bool
    force_score: bool
    added_time: datetime
    update_time: datetime
    submission: Union[Submission, None]
    verdict_of_submission: Union[VerdictOfSubmission, None]


class BaseSolution(BaseModel):
    id: int
    score: int
    status: Status
    deadline: datetime
    task: BaseTask
    student: BaseUser
    added_time: datetime
    update_time: datetime
    has_activity_after_deadline: bool
    latest_submission: Union[Submission, None]
    submissions_count: int
    is_score_max: bool


class Solution(BaseModel):
    solution: BaseSolution
    file: Optional[File]
    comments: List[Comment]
