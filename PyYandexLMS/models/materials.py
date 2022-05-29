from PyYandexLMS.models.base import BaseMaterial, BaseModel
from PyYandexLMS.models.lesson import BaseLesson


class DetailedMaterial(BaseMaterial):
    content: str


class MaterialInformation(BaseModel):
    detailed_material: DetailedMaterial
    lesson: BaseLesson
