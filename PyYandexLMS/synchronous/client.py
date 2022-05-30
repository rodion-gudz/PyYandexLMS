import os
import pickle
from typing import List, Union

from requests import Session

from PyYandexLMS.errors import AuthError
from PyYandexLMS.models.course import Course
from PyYandexLMS.models.lesson import BaseLesson, Lesson
from PyYandexLMS.models.materials import BaseMaterial, MaterialInformation
from PyYandexLMS.models.notification import NotificationInformation
from PyYandexLMS.models.profile import ProfileInformation
from PyYandexLMS.models.solution import BaseSolution, SolutionInformation
from PyYandexLMS.models.task import Task, TaskType


class Client(Session):
    def __init__(self, login: str, password: str, session_name: str = None):
        """
        Сессия Yandex Lyceum API. Основана на Requests session.

        :param login: Почта Yandex
        :param password: Пароль аккаунта
        :param session_name: Имя файла для сохранения сессии. По умолчанию {login}.session
        """
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
        """Проверка авторизации пользователя"""

        return self.get("https://api.passport.yandex.ru/all_accounts").text != "{}"

    def get_user(
        self,
        with_courses_summary: bool = True,
        with_expelled: bool = True,
        with_children: bool = True,
        with_parents: bool = True,
    ) -> ProfileInformation:
        """
        Возвращает информацию о пользователе в виде объекта UserInformation.

        :param with_courses_summary: Получить информацию о курсах пользователя
        :param with_expelled: Включить информацию о законченных курсах
        :param with_children: Показать информацию о детях (Если пользователь - родитель)
        :param with_parents: Показать информацию о родителях (Если пользователь - ребенок)
        """

        return ProfileInformation.parse_obj(
            self.get(
                "https://lyceum.yandex.ru/api/profile",
                params={
                    "withCoursesSummary": with_courses_summary,
                    "withExpelled": with_expelled,
                    "withChildren": with_children,
                    "withParents": with_parents,
                },
            ).json()
        )

    def get_lessons(
        self,
        course: Course = None,
        course_id: int = None,
        group_id: int = None,
    ) -> List[BaseLesson]:
        """
        Возвращает список уроков в курсе.

        Необходимо передать объект курса или course_id + group_id.

        :param course: Объект кура (Course)
        :param course_id: Идентификатор курса
        :param group_id: Идентификатор группы
        """

        if course:
            course_id = course.id
            group_id = course.group.id

        if not course_id or not group_id:
            raise ValueError(
                "Необходимо передать объект курса или course_id + group_id"
            )

        lessons = self.get(
            "https://lyceum.yandex.ru/api/student/lessons/",
            params={"courseId": course_id, "groupId": group_id},
        ).json()

        return [BaseLesson.parse_obj(lesson) for lesson in lessons]

    def get_lesson(self, lesson_id: int, course_id: int, group_id: int) -> Lesson:
        """
        Возвращает информацию о уроке.

        :param lesson_id: Идентификатор урока
        :param course_id: Идентификатор курса
        :param group_id: Идентификатор группы
        """

        return Lesson.parse_obj(
            self.get(
                f"https://lyceum.yandex.ru/api/student/lessons/{lesson_id}",
                params={"courseId": course_id, "groupId": group_id},
            ).json()
        )

    def get_tasks(
        self, lesson_id: int, course_id: int, group_id: int
    ) -> List[TaskType]:
        """
        Возвращает список заданий в уроке.

        :param lesson_id: Идентификатор урока
        :param course_id: Идентификатор курса
        :param group_id: Идентификатор группы
        """
        tasks = self.get(
            "https://lyceum.yandex.ru/api/student/lessonTasks",
            params={"courseId": course_id, "groupId": group_id, "lessonId": lesson_id},
        ).json()

        return [TaskType.parse_obj(task_type) for task_type in tasks]

    def get_task(self, task_id: int, group_id: int) -> Task:
        """
        Возвращает информацию о задании.

        :param task_id: Идентификатор задания
        :param group_id: Идентификатор группы
        """

        return Task.parse_obj(
            self.get(
                f"https://lyceum.yandex.ru/api/student/tasks/{task_id}",
                params={"groupId": group_id},
            ).json()
        )

    def get_materials(
        self, lesson: Union[Lesson, BaseLesson] = None, lesson_id: int = None
    ) -> List[BaseMaterial]:
        """
        Возвращает список материалов в уроке.

        Необходимо передать объект урока или lesson_id.

        :param lesson: Объект урока (Lesson или BaseLesson)
        :param lesson_id: Идентификатор урока
        """

        if lesson:
            lesson_id = lesson.id

        materials = self.get(
            "https://lyceum.yandex.ru/api/materials/", params={"lessonId": lesson_id}
        ).json()

        return [BaseMaterial.parse_obj(material) for material in materials]

    def get_material(
        self,
        material_id: int = None,
        group_id: int = None,
        lesson_id: int = None,
    ) -> MaterialInformation:
        """
        Возвращает информацию о материале по его идентификатору.

        :param material_id: Идентификатор материала
        :param lesson_id: Идентификатор урока
        :param group_id: Идентификатор группы
        """

        return MaterialInformation.parse_obj(
            self.get(
                f"https://lyceum.yandex.ru/api/student/materials/{material_id}",
                params={"groupId": group_id, "lessonId": lesson_id},
            ).json()
        )

    def get_solution(
        self, solution: BaseSolution = None, solution_id: int = None
    ) -> SolutionInformation:
        """
        Возвращает информацию о решении.

        Необходимо передать объект решения или solution_id.

        :param solution: Объект решения (BaseSolution)
        :param solution_id: Идентификатор решения
        """

        if solution:
            solution_id = solution.id

        return SolutionInformation.parse_obj(
            self.get(
                f"https://lyceum.yandex.ru/api/student/solutions/{solution_id}"
            ).json()
        )

    def get_notifications(self, is_read: bool = False) -> NotificationInformation:
        """Возвращает список уведомлений пользователя

        :param is_read: Показать уведомления, которые уже прочитаны
        """

        return NotificationInformation.parse_obj(
            self.get(
                "https://lyceum.yandex.ru/api/notifications",
                params={"isRead": is_read},
            ).json()
        )
