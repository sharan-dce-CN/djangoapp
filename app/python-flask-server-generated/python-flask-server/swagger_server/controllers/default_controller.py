import connexion
import six

from swagger_server.models.assign import Assign  # noqa: E501
from swagger_server.models.assign_as_mentor import AssignAsMentor  # noqa: E501
from swagger_server.models.assign_users import AssignUsers  # noqa: E501
from swagger_server.models.project import Project  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server import util


def project_assign_post(project_id=None):  # noqa: E501
    """Assign a Project to multiple users

     # noqa: E501

    :param project_id: ID of Project and list of users
    :type project_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        project_id = Assign.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def project_assign_users_post(users=None):  # noqa: E501
    """Assign users to a project

     # noqa: E501

    :param users: ID of Project and List of IDs of Users
    :type users: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        users = AssignUsers.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def project_post(name=None):  # noqa: E501
    """Create New Project

     # noqa: E501

    :param name: Name of the Project
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = Project.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def project_project_get_mentors_get(project):  # noqa: E501
    """Get the mentors of a project

     # noqa: E501

    :param project: ID of Project
    :type project: int

    :rtype: None
    """
    return 'do some magic!'


def project_project_get_users_mentors_get(project):  # noqa: E501
    """Get the users and mentors in a project

     # noqa: E501

    :param project: ID of Project
    :type project: int

    :rtype: None
    """
    return 'do some magic!'


def root_get():  # noqa: E501
    """Root Page

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def user_assign_as_mentor_post(mentor=None):  # noqa: E501
    """Assign Mentor to a Project

     # noqa: E501

    :param mentor: ID of Mentor and Project
    :type mentor: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        mentor = AssignAsMentor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_post(name=None):  # noqa: E501
    """Create New User

     # noqa: E501

    :param name: Name of the User
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_user_mentees_get(user):  # noqa: E501
    """Get Mentees of a User

     # noqa: E501

    :param user: ID of User
    :type user: int

    :rtype: None
    """
    return 'do some magic!'


def user_user_projects_mentoring_get(user):  # noqa: E501
    """Get list of projects mentored by a user

     # noqa: E501

    :param user: ID of User
    :type user: int

    :rtype: None
    """
    return 'do some magic!'
