# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.assign import Assign  # noqa: E501
from swagger_server.models.assign_as_mentor import AssignAsMentor  # noqa: E501
from swagger_server.models.assign_users import AssignUsers  # noqa: E501
from swagger_server.models.project import Project  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_project_assign_post(self):
        """Test case for project_assign_post

        Assign a Project to multiple users
        """
        project_id = Assign()
        response = self.client.open(
            '/polls/project/assign',
            method='POST',
            data=json.dumps(project_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_assign_users_post(self):
        """Test case for project_assign_users_post

        Assign users to a project
        """
        users = AssignUsers()
        response = self.client.open(
            '/polls/project/assign-users',
            method='POST',
            data=json.dumps(users),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_post(self):
        """Test case for project_post

        Create New Project
        """
        name = Project()
        response = self.client.open(
            '/polls/project',
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_project_get_mentors_get(self):
        """Test case for project_project_get_mentors_get

        Get the mentors of a project
        """
        response = self.client.open(
            '/polls/project/{project}/get-mentors'.format(project=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_project_get_users_mentors_get(self):
        """Test case for project_project_get_users_mentors_get

        Get the users and mentors in a project
        """
        response = self.client.open(
            '/polls/project/{project}/get-users-mentors'.format(project=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_root_get(self):
        """Test case for root_get

        Root Page
        """
        response = self.client.open(
            '/polls/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_assign_as_mentor_post(self):
        """Test case for user_assign_as_mentor_post

        Assign Mentor to a Project
        """
        mentor = AssignAsMentor()
        response = self.client.open(
            '/polls/user/assign-as-mentor',
            method='POST',
            data=json.dumps(mentor),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_post(self):
        """Test case for user_post

        Create New User
        """
        name = User()
        response = self.client.open(
            '/polls/user',
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_mentees_get(self):
        """Test case for user_user_mentees_get

        Get Mentees of a User
        """
        response = self.client.open(
            '/polls/user/{user}/mentees'.format(user=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_user_projects_mentoring_get(self):
        """Test case for user_user_projects_mentoring_get

        Get list of projects mentored by a user
        """
        response = self.client.open(
            '/polls/user/{user}/projects-mentoring'.format(user=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
