from PyYandexLMS.models.base.main import BaseModel


class User(BaseModel):
    id: int
    uid: int
    username: str
    last_name: str
    first_name: str
    middle_name: str
    display_name: str
    avatar: str
    gender: str
