from datetime import datetime
from typing import List, Union

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.file import File
from PyYandexLMS.models.submission import Submission
from PyYandexLMS.models.user import User
from PyYandexLMS.models.verdict import Verdict


class Comment(BaseModel):
    id: int
    author: User
    type: str
    data: str
    files: List[File]
    is_changed: bool
    force_score: bool
    added_time: datetime
    update_time: datetime
    submission: Union[Submission, None]
    verdict_of_submission: Union[Verdict, None]
