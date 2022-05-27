import os
import pickle

from requests import Session

from PyYandexLMS.errors import AuthError
from PyYandexLMS.models import User


class Client(Session):
    def __init__(self, login, password, session_name=None):
        super().__init__()
        session_name = session_name or f"{login}.session"
        if not os.path.exists(session_name):
            if (
                self.post(
                    "https://passport.yandex.ru/passport?mode=auth",
                    data={"login": login, "passwd": password},
                ).url
                != "https://passport.yandex.ru/profile"
            ):
                raise AuthError("Ошибка авторизации (Неверные данные или включен 2FA)")
            with open(session_name, "wb") as f:
                pickle.dump(self.cookies, f)
        else:
            with open(session_name, "rb") as f:
                self.cookies = pickle.load(f)

    def check_authorized(self):
        return self.get("https://api.passport.yandex.ru/all_accounts").text != "{}"

    def get_user(
        self,
        with_courses_summary: bool = True,
        with_expelled: bool = True,
        with_children: bool = True,
        with_parents: bool = True,
    ) -> User:
        return User.parse_obj(
            self.get(
                "https://lyceum.yandex.ru/api/profile",
                params={
                    "withCoursesSummary": str(with_courses_summary).lower(),
                    "withExpelled": str(with_expelled).lower(),
                    "withChildren": str(with_children).lower(),
                    "withParents": str(with_parents).lower(),
                },
            ).json()
        )
