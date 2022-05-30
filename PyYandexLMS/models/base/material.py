from PyYandexLMS.models.base.main import BaseModel


class BaseMaterial(BaseModel):
    id: int
    type: str
    title: str
