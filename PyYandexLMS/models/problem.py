from typing import List, Optional, Union, Dict

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.layout import Layout
from PyYandexLMS.models.resource import Resource
from PyYandexLMS.models.status import Status
from PyYandexLMS.models.tag import Tag


class Markup(BaseModel):
    checks: Union[Dict, None]
    layout: List[Layout]
    answers: Union[Dict, None]


class Problem(BaseModel):
    id: int
    markup: Markup
    resources: Dict[str, Resource]


class ProblemSolution(BaseModel):
    id: Optional[int]
    is_success: Optional[bool]
    score: Optional[float]
    is_closed: Optional[bool]
    status: Status


class ProblemInformation(BaseModel):
    title: str
    id: int
    tag: Tag
    score_max: int
    attempts_max: int
    solution: Optional[ProblemSolution]
    problem: Problem
