from datetime import datetime
from typing import Union, Optional

from PyYandexLMS.models.base import BaseModel
from PyYandexLMS.models.lesson import BaseLesson


class BaseMaterial(BaseModel):
    id: int
    type: str
    title: str


class DetailedMaterial(BaseMaterial):
    content: str


class Material(BaseModel):
    detailed_material: DetailedMaterial
    lesson: BaseLesson
