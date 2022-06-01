from typing import List, Optional, Union

from PyYandexLMS.models.base.main import BaseModel
from PyYandexLMS.models.base.profile import BaseProfile
from PyYandexLMS.models.course import CoursesSummary
from PyYandexLMS.models.group import Group
from PyYandexLMS.models.invite import Invite
from PyYandexLMS.models.placement import Placement


class Profile(BaseProfile):
    children: Union[List[BaseProfile], None]
    parents: Union[List[BaseProfile], None]
    groups: List[Group]
    permissions: List[str]
    managed_cities: List[str]
    managed_venues: List[str]
    city_to_managed_venues: List[str]
    invite: Optional[Invite]


class ProfileInformation(BaseModel):
    profile: Profile
    courses_summary: Union[CoursesSummary, None]
    placement: Placement
