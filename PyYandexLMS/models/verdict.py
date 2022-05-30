from datetime import datetime
from typing import Union

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.file import File


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
