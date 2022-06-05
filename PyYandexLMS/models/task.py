from typing import List, Optional, Union

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.base.task import BaseTask
from PyYandexLMS.models.problem import DetailedProblem
from PyYandexLMS.models.submission import Submission
from PyYandexLMS.models.variant import Variant


class Task(BaseTask):
    variant: Variant
    description: str
    compilers_ids: List[int]
    solution_id: int
    latest_submission: Union[Submission, None]


class TaskType(BaseModel):
    id: int
    type: str
    color: str
    order: int
    tasks: Optional[List[BaseTask]]
    problems: Optional[List[DetailedProblem]]
