from datetime import datetime
from typing import Optional

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.status import Status


class BaseSolution(BaseModel):
    id: int
    score: int
    status: Status
    task_id: Optional[int]
    added_time: datetime
    update_time: datetime
