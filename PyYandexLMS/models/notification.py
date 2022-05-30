from datetime import datetime
from typing import Dict, List, Optional

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.lesson import NotificationLesson
from PyYandexLMS.models.status import Status


class NotificationTask(BaseModel):
    id: int
    group: int
    title: str
    course: int
    lesson: NotificationLesson
    score_max: int
    short_title: str


class TaskSolution(BaseModel):
    id: int
    task: NotificationTask
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
