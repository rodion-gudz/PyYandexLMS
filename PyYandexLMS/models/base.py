from pydantic import BaseModel as PydanticBaseModel

from PyYandexLMS.utils.validation import to_camel_case


class BaseModel(PydanticBaseModel):
    class Config:
        alias_generator = to_camel_case
