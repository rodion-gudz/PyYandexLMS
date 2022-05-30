from typing import Union

from PyYandexLMS.models.base.main import BaseModel


class Placement(BaseModel):
    venue: Union[str, None]
    city: Union[str, None]
