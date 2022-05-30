from PyYandexLMS.models.base.main import BaseModel


class Invite(BaseModel):
    url: str
    uses_count: int
    uses_limit: int
