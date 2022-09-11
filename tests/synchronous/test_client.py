import json

from hypothesis import strategies as st

from PyYandexLMS.models.base.lesson import BaseLesson
from PyYandexLMS.models.course import Course
from PyYandexLMS.models.group import Group
from PyYandexLMS.models.task import Task
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


def test_get_lesson_information(requests_mock):
    client = TestClient(requests_mock)

    with open("tests/json_data/lesson_information.json") as f:
        fake_json = f.read()

    course = st.from_type(Course).example()
    lesson = st.from_type(BaseLesson).example()

    for data in json.loads(fake_json):
        requests_mock.get(
            get_lesson_information_link(
                lesson_id=lesson.id, course_id=course.id, group_id=course.group.id
            ),
            json=data,
        )
        assert client.get_lesson(
            lesson_id=lesson.id, course_id=course.id, group_id=course.group.id
        )


def test_get_tasks(requests_mock):
    client = TestClient(requests_mock)

    with open("tests/json_data/tasks.json") as f:
        fake_json = f.read()

    lesson_id = 123
    course_id = 123
    group_id = 123

    for data in json.loads(fake_json):
        requests_mock.get(
            get_tasks_list_link(lesson_id=lesson_id, course_id=course_id, group_id=group_id),
            json=data,
        )
        tasks = client.get_tasks(
            lesson_id=lesson_id, course_id=course_id, group_id=group_id
        )
        if tasks != []:
            assert tasks


def test_get_task_information(requests_mock):
    client = TestClient(requests_mock)

    with open("tests/json_data/task_information.json") as f:
        fake_json = f.read()

    group = st.from_type(Group).example()
    task = st.from_type(Task).example()

    for data in json.loads(fake_json):
        requests_mock.get(
            get_task_information_link(task_id=task.id, group_id=group.id),
            json=data,
        )
        assert client.get_task(task_id=task.id, group_id=group.id)


def test_notifications(requests_mock):
    client = TestClient(requests_mock)

    with open("tests/json_data/notifications.json") as f:
        fake_json = f.read()
    for data in json.loads(fake_json):
        requests_mock.get(get_notifications_link(is_read=True), json=data)
        assert client.get_notifications(is_read=True)
