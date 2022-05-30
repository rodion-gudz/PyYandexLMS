from PyYandexLMS.models.base.main import BaseModel


class Tag(BaseModel):
    id: int
    type: str
    color: str
    order: int
