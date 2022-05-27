from aiohttp import ClientSession


class Client(ClientSession):
    def __init__(self, login, password, session_name=None):
        super().__init__()
