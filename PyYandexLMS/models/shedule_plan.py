from datetime import date, time
from typing import List

from PyYandexLMS.models.base.main import BaseModel


class SchedulePlanItem(BaseModel):
    id: int
    schedule_plan: int
    day_of_week: int
    start_time: time


class SchedulePlan(BaseModel):
    id: int
    group: int
    study_period: int
    start_date: date
    items: List[SchedulePlanItem]
