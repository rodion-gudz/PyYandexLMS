from urllib.parse import urlencode


def get_user_information_link(
    with_courses_summary: bool = True,
    with_expelled: bool = True,
    with_children: bool = True,
    with_parents: bool = True,
):
    params = {
        "withCoursesSummary": with_courses_summary,
        "withExpelled": with_expelled,
        "withChildren": with_children,
        "withParents": with_parents,
    }
    return f"https://lyceum.yandex.ru/api/profile?{urlencode(params)}"


def get_lessons_list_link(course_id: int, group_id: int) -> str:
    params = {"courseId": course_id, "groupId": group_id}
    return f"https://lyceum.yandex.ru/api/student/lessons?{urlencode(params)}"


def get_lesson_information_link(lesson_id: int, course_id: int, group_id: int) -> str:
    params = {"courseId": course_id, "groupId": group_id}
    return (
        f"https://lyceum.yandex.ru/api/student/lessons/{lesson_id}?{urlencode(params)}"
    )


def get_tasks_list_link(lesson_id: int, course_id: int) -> str:
    params = {"courseId": course_id, "lessonId": lesson_id}
    return f"https://lyceum.yandex.ru/api/student/lessonTasks?{urlencode(params)}"


def get_task_information_link(task_id: int, group_id: int) -> str:
    params = {"groupId": group_id}
    return f"https://lyceum.yandex.ru/api/student/tasks/{task_id}?{urlencode(params)}"


def get_materials_list_link(lesson_id: int) -> str:
    params = {"lessonId": lesson_id}
    return f"https://lyceum.yandex.ru/api/materials?{urlencode(params)}"


def get_material_information_link(
    material_id: int,
    group_id: int,
    lesson_id: int,
) -> str:
    params = {"groupId": group_id, "lessonId": lesson_id}
    return f"https://lyceum.yandex.ru/api/student/materials/{material_id}?{urlencode(params)}"


def get_solution_information_link(solution_id: int) -> str:
    return f"https://lyceum.yandex.ru/api/student/solutions/{solution_id}"


def get_problem_detail_link(solution_id: int) -> str:
    params = {"solutionId": solution_id}
    return f"https://lyceum.yandex.ru/api/problem/details?{urlencode(params)}"


def get_notifications_link(is_read: bool = False) -> str:
    params = {"isRead": is_read}
    return f"https://lyceum.yandex.ru/api/notifications?{urlencode(params)}"
