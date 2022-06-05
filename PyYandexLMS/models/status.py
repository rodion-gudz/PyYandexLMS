from typing import Optional

from PyYandexLMS.models.base.main import BaseModel


class Status(BaseModel):
    id: Optional[int]
    type: str
