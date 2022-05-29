from datetime import datetime
from typing import Optional

from pydantic import BaseModel as PydanticBaseModel

from PyYandexLMS.utils.validation import to_camel_case


class BaseModel(PydanticBaseModel):
    class Config:
        alias_generator = to_camel_case


class Status(BaseModel):
    id: int
    type: str


class Group(BaseModel):
    id: int
    name: str


class BaseUser(BaseModel):
    id: int
    uid: int
    username: str
    last_name: str
    first_name: str
    middle_name: str
    display_name: str
    avatar: str
    gender: str


class BaseSolution(BaseModel):
    id: int
    score: int
    status: Status
    task_id: Optional[int]
    added_time: datetime
    update_time: datetime


class BaseLesson(BaseModel):
    id: int
    short_title: str
    title: str
    type: str
    num_tasks: Optional[int]
    num_passed: Optional[int]
    deadline: Optional[datetime]
    ms_before_deadline: Optional[int]
    has_assigned_variant: Optional[bool]
    manual_variants_assignment: Optional[bool]


class BaseMaterial(BaseModel):
    id: int
    type: str
    title: str
