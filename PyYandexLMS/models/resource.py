from datetime import datetime

from PyYandexLMS.models.base.main import BaseModel


class Resource(BaseModel):
    id: int
    url: str
    image_width: int
    image_height: int
    name: str
    type: str
    version: int
    date_updated: datetime
