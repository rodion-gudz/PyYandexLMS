from typing import Optional, Dict, List

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.input import Input


class LayoutOptions(BaseModel):
    text: Optional[str]
    inputs: Optional[Dict[str, Input]]
    flavor: Optional[str]
    choices: Optional[List[str]]
    type_display: Optional[str]


class LayoutContent(BaseModel):
    id: Optional[int]
    type: Optional[str]
    text: Optional[str]
    options: Optional[LayoutOptions]


class Layout(BaseModel):
    kind: str
    content: LayoutContent
