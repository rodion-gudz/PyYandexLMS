from datetime import datetime
from typing import Optional, Union

from PyYandexLMS.models.base.main import BaseModel


class File(BaseModel):
    id: int
    name: str
    url: str
    mime_type: str
    encoding: str
    size: int
    run_id: Union[str, None]
    added_time: datetime
    source_code: Optional[str]
