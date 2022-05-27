import os
import pickle

from aiohttp import ClientSession

from PyYandexLMS.errors import AuthError


class Client(ClientSession):
    def __init__(self, login, password, session_name=None):
        super().__init__()
        session_name = session_name or f"{login}.session"
        if not os.path.exists(session_name):
            if (
                await self.post(
                    "https://passport.yandex.ru/passport?mode=auth",
                    data={"login": login, "passwd": password},
                )
            ).url != "https://passport.yandex.ru/profile":
                raise AuthError("Ошибка авторизации (Неверные данные или включен 2FA)")
            with open(session_name, "wb") as f:
                pickle.dump(self.cookies, f)
        else:
            with open(session_name, "rb") as f:
                self.cookies = pickle.load(f)

    async def check_authorized(self):
        return (
            await self.get("https://api.passport.yandex.ru/all_accounts")
        ).text != "{}"
