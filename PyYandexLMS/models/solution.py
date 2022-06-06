from datetime import datetime
from typing import List, Optional, Union

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.base.solution import BaseSolution
from PyYandexLMS.models.comment import Comment
from PyYandexLMS.models.file import File
from PyYandexLMS.models.submission import Submission
from PyYandexLMS.models.task import BaseTask
from PyYandexLMS.models.user import User


class Solution(BaseSolution):
    deadline: Union[datetime, None]
    task: BaseTask
    student: User
    has_activity_after_deadline: bool
    latest_submission: Union[Submission, None]
    submissions_count: int
    is_score_max: bool


class SolutionInformation(BaseModel):
    solution: Solution
    file: Optional[File]
    comments: List[Comment]
