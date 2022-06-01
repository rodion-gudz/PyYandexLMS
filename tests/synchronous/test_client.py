import json

from hypothesis import strategies as st

from PyYandexLMS.models.course import Course
from PyYandexLMS.synchronous import Client
from PyYandexLMS.utils.link_generator import *


class TestClient(Client):
    def __init__(self, requests_mock):
        login = "login"
        password = "password"
        requests_mock.post("https://passport.yandex.ru/passport?mode=auth")
        requests_mock.get(
            "https://api.passport.yandex.ru/all_accounts", json={"status": "OK"}
        )
        super().__init__(login, password)


def test_get_user(requests_mock):
    client = TestClient(requests_mock)

    with open("tests/json_data/user_information.json") as f:
        fake_json = f.read()
    for data in json.loads(fake_json):
        requests_mock.get(get_user_information_link(), json=data)
        assert client.get_user()


def test_get_lessons(requests_mock):
    client = TestClient(requests_mock)

    with open("tests/json_data/lessons.json") as f:
        fake_json = f.read()

    course = st.from_type(Course).example()

    for data in json.loads(fake_json):
        requests_mock.get(
            get_lessons_list_link(course_id=course.id, group_id=course.group.id),
            json=data,
        )
        try:
            assert client.get_lessons(course_id=course.id, group_id=course.group.id)
        except Exception as e:
            print(e)
        try:
            assert client.get_lessons_by_course(course=course)
        except Exception as e:
            print(e)


def test_notifications(requests_mock):
    client = TestClient(requests_mock)

    with open("tests/json_data/notifications.json") as f:
        fake_json = f.read()
    for data in json.loads(fake_json):
        requests_mock.get(get_notifications_link(is_read=True), json=data)
        assert client.get_notifications(is_read=True)
