from datetime import datetime

from PyYandexLMS.models.base.main import BaseModel


class File(BaseModel):
    id: int
    name: str
    url: str
    mime_type: str
    encoding: str
    size: int
    run_id: str
    added_time: datetime
