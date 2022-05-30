from datetime import datetime
from typing import Union

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.file import File


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
