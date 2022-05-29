from pprint import pprint
from typing import List

from PyYandexLMS.models.course import Course


def print_courses(courses: List[Course]):
    for course in courses:
        print(f"Курс {course.title}:")
        pprint(course.dict())
