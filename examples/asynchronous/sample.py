import asyncio
from os import getenv

from PyYandexLMS.asynchronous import Client

login = getenv("LOGIN")
password = getenv("PASSWORD")


async def main():
    client = Client(login, password)
    # In development


if __name__ == "__main__":
    asyncio.run(main())
