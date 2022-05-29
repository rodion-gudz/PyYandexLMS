from datetime import datetime
from typing import Dict, List, Optional

from PyYandexLMS.models.base import BaseModel, Status


class Lesson(BaseModel):
    id: int
    type: str
    title: str
    is_accepted: bool
    short_title: str


class Task(BaseModel):
    id: int
    group: int
    title: str
    course: int
    lesson: Lesson
    score_max: int
    short_title: str


class TaskSolution(BaseModel):
    id: int
    task: Task
    score: int
    status: Status


class ObjectData(BaseModel):
    verdict: Optional[str]
    comment_id: Optional[int]
    task_solution: Optional[TaskSolution]


class Notification(BaseModel):
    id: int
    is_read: bool
    type: str
    object_data: ObjectData
    added_time: datetime


class NotificationInformation(BaseModel):
    notification_map: Dict[int, Notification]
    notification_ids: List[int]
    unread_count: int
