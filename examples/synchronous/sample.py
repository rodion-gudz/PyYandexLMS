from os import getenv

from PyYandexLMS.synchronous.client import Client

login = getenv("LOGIN")
password = getenv("PASSWORD")


def main():
    client = Client(login, password)
    print(client.check_authorized())


if __name__ == "__main__":
    main()
