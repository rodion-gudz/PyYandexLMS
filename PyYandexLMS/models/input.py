from PyYandexLMS.models.base.main import BaseModel


class InputOptions(BaseModel):
    width: int
    type_content: str


class Input(BaseModel):
    type: str
    group: int
    options: InputOptions
