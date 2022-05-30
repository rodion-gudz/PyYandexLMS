from typing import Optional

from PyYandexLMS.models.base.main import BaseModel


class Progress(BaseModel):
    num_tasks: Optional[int]
    num_passed: Optional[int]
    num_rework: Optional[int]
