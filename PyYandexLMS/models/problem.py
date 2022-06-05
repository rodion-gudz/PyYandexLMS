from datetime import datetime
from typing import List, Optional, Union, Dict

from PyYandexLMS.models.base.lesson import BaseLesson
from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.layout import Layout
from PyYandexLMS.models.resource import Resource
from PyYandexLMS.models.status import Status
from PyYandexLMS.models.tag import Tag


class CheckSource(BaseModel):
    type: str
    source: int


class CheckSourcesList(BaseModel):
    type: str
    sources: List[CheckSource]


class Check(BaseModel):
    type: str
    sources: List[CheckSourcesList]


class Markup(BaseModel):
    checks: Union[Dict[str, Dict[str, Check]], None]
    layout: List[Layout]
    answers: Union[Dict[str, Dict[str, List[str]]], None]


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


class DetailedProblem(BaseModel):
    title: str
    id: int
    tag: Tag
    score_max: int
    attempts_max: int
    solution: Optional[ProblemSolution]
    problem: Problem


class ProblemSubmission(BaseModel):
    id: int
    submission: Dict[str, Dict[str, str]]
    score: int
    date: datetime


class ProblemInformation(BaseModel):
    title: str
    tag: Tag
    score_max: int
    attempts_max: int
    problem: Problem
    solution: Optional[ProblemSolution]
    submissions: List[ProblemSubmission]
    lesson: BaseLesson
