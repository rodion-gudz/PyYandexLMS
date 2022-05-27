import asyncio
from os import getenv

from PyYandexLMS.asynchronous.client import Client

login = getenv("LOGIN")
password = getenv("PASSWORD")


async def main():
    client = Client(login, password)
    print(await client.check_authorized())


if __name__ == "__main__":
    asyncio.run(main())
