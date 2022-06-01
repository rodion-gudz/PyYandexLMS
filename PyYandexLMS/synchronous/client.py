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
from PyYandexLMS.utils.link_generator import *


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
            self.post(
                "https://passport.yandex.ru/passport?mode=auth",
                data={"login": login, "passwd": password},
            )
            if not self.check_authorized():
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
                get_user_information_link(
                    with_courses_summary=with_courses_summary,
                    with_expelled=with_expelled,
                    with_children=with_children,
                    with_parents=with_parents,
                )
            ).json()
        )

    def get_lessons(
        self,
        course_id: int,
        group_id: int,
    ) -> List[BaseLesson]:
        """
        Возвращает список уроков в курсе.

        :param course_id: Идентификатор курса
        :param group_id: Идентификатор группы
        """

        lessons = self.get(
            get_lessons_list_link(
                course_id=course_id,
                group_id=group_id,
            )
        ).json()

        return [BaseLesson.parse_obj(lesson) for lesson in lessons]

    def get_lessons_by_course(self, course: Course) -> List[BaseLesson]:
        """
        Возвращает список уроков в курсе.

        :param course: Объект курса (Course)
        """

        return self.get_lessons(course_id=course.id, group_id=course.group.id)

    def get_lesson(self, lesson_id: int, course_id: int, group_id: int) -> Lesson:
        """
        Возвращает информацию о уроке.

        :param lesson_id: Идентификатор урока
        :param course_id: Идентификатор курса
        :param group_id: Идентификатор группы
        """

        return Lesson.parse_obj(
            self.get(
                get_lesson_information_link(
                    lesson_id=lesson_id,
                    course_id=course_id,
                    group_id=group_id,
                )
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
            get_tasks_list_link(
                lesson_id=lesson_id,
                course_id=course_id,
                group_id=group_id,
            )
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
                get_task_information_link(
                    task_id=task_id,
                    group_id=group_id,
                )
            ).json()
        )

    def get_materials(self, lesson_id: int) -> List[BaseMaterial]:
        """
        Возвращает список материалов в уроке.

        :param lesson_id: Идентификатор урока
        """

        materials = self.get(
            get_materials_list_link(lesson_id=lesson_id),
        ).json()

        return [BaseMaterial.parse_obj(material) for material in materials]

    def get_materials_by_lesson(self, lesson: Union[Lesson, BaseLesson]):
        """
        Возвращает список материалов в уроке.

        :param lesson: Объект урока (Lesson или BaseLesson)
        """

        return self.get_materials(lesson_id=lesson.id)

    def get_material(
        self,
        material_id: int,
        group_id: int,
        lesson_id: int,
    ) -> MaterialInformation:
        """
        Возвращает информацию о материале по его идентификатору.

        :param material_id: Идентификатор материала
        :param lesson_id: Идентификатор урока
        :param group_id: Идентификатор группы
        """

        return MaterialInformation.parse_obj(
            self.get(
                get_material_information_link(
                    material_id=material_id, lesson_id=lesson_id, group_id=group_id
                )
            ).json()
        )

    def get_solution_information(self, solution_id: int) -> SolutionInformation:
        """
        Возвращает информацию о решении.

        :param solution_id: Идентификатор решения
        """

        return SolutionInformation.parse_obj(
            self.get(get_solution_information_link(solution_id=solution_id)).json()
        )

    def get_solution_information_by_solution(
        self, solution: BaseSolution
    ) -> SolutionInformation:
        """
        Возвращает информацию о решении.

        :param solution: Объект решения BaseSolution
        """

        return self.get_solution_information(solution_id=solution.id)

    def get_notifications(self, is_read: bool = False) -> NotificationInformation:
        """Возвращает список уведомлений пользователя

        :param is_read: Показать уведомления, которые уже прочитаны
        """

        return NotificationInformation.parse_obj(
            self.get(get_notifications_link(is_read=is_read)).json()
        )
