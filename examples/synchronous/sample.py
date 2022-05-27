from os import getenv

from PyYandexLMS.synchronous.client import Client

login = getenv("LOGIN")
password = getenv("PASSWORD")


def main():
    client = Client(login, password)
    user = client.get_user()
    print(f"Имя: {user.profile.display_name}")
    print(f"Дата регистрации в LMS: {user.profile.date_joined.strftime('%d.%m.%Y')}")
    print(
        f"Курсы: {', '.join(course.title for course in user.courses_summary.student)}"
    )


if __name__ == "__main__":
    main()
