from typing import Any, Union

from PyYandexLMS.models.base.main import BaseModel


class Placement(BaseModel):
    venue: Union[Any, None]
    city: Union[Any, None]
