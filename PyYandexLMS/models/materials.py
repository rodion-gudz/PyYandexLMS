from PyYandexLMS.models.base import BaseModel, BaseMaterial
from PyYandexLMS.models.lesson import BaseLesson


class DetailedMaterial(BaseMaterial):
    content: str


class MaterialInformation(BaseModel):
    detailed_material: DetailedMaterial
    lesson: BaseLesson
