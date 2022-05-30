from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.base.material import BaseMaterial
from PyYandexLMS.models.lesson import BaseLesson


class Material(BaseMaterial):
    content: str


class MaterialInformation(BaseModel):
    detailed_material: Material
    lesson: BaseLesson
