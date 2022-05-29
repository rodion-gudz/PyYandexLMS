from datetime import datetime
from typing import List, Optional, Union

from PyYandexLMS.models.base import BaseModel, BaseSolution
from PyYandexLMS.models.task import File, Submission, BaseTask
from PyYandexLMS.models.user import BaseUser


class Verdict(BaseModel):
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
    verdict_of_submission: Union[Verdict, None]


class Solution(BaseSolution):
    deadline: datetime
    task: BaseTask
    student: BaseUser
    has_activity_after_deadline: bool
    latest_submission: Union[Submission, None]
    submissions_count: int
    is_score_max: bool


class SolutionInformation(BaseModel):
    solution: Solution
    file: Optional[File]
    comments: List[Comment]
