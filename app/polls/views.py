from django.core.serializers import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from rest_framework.decorators import api_view

from .models import *

def invalid_data(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            return HttpResponse(error)
    return wrapper

@csrf_exempt
@invalid_data
@api_view(["POST"])
@require_http_methods("POST")
def create_user(record):
    """
    Create New User
    """
    json_data = json.loads(record.body.decode('utf-8'))
    instance = User(Name = json_data['name'] + "")
    instance.save()
    return HttpResponse(status = 201)

@csrf_exempt
@invalid_data
@api_view(["POST"])
@require_http_methods("POST")
def create_project(record):
    """
    Create New Project
    """
    json_data = json.loads(record.body.decode('utf-8'))
    instance = Project(Name = json_data['name'] + "")
    instance.save()
    return HttpResponse(status = 201)

@csrf_exempt
@api_view(["GET"])
@require_http_methods("GET")
def root(request):
    """
    Root
    """
    return HttpResponse('This is the root page of the app')


@csrf_exempt
@invalid_data
@api_view(["POST"])
@require_http_methods("POST")
def assign_project_to_users(record):     #assign project to users
    """
    Assign 1 Project to Users
    """
    instance = jsonface.loads(record.body.decode('utf-8'))
    project_id = instance['project_id'] + 0
    users = instance['users'] + []
    for user in users:
        instance = Project_User(Project_id = Project.objects.get(id = project_id), User_id = User.objects.get(id = user))
        instance.save()
    return HttpResponse(status = 201)

@csrf_exempt
@invalid_data
@api_view(["POST"])
@require_http_methods("POST")
def assign_mentor(record):      #assign one user as mentor to a project
    """
    Assign a Mentor to a Project
    """
    instance = json.loads(record.body.decode('utf-8'))
    user = instance['mentor'] + 0
    project = instance['project'] + 0
    instance = Project_User(Project_id = Project.objects.get(id = project), User_id = User.objects.get(id = user), IsMentor = True)
    instance.save()
    return HttpResponse(status = 201)


@csrf_exempt
@invalid_data
@api_view(["POST"])
@require_http_methods("POST")
def assign_users_to_project(record):      #assign users to a project
    """
    Assign Users to a single Project
    """
    instance = json.loads(record.body.decode('utf-8'))
    project = instance['project'] + 0
    users = instance['users'] + []
    for user in users:
        instance = Project_User(Project_id = Project.objects.get(id = project), User_id = User.objects.get(id = user))
        instance.save()
    return HttpResponse(status = 201)


@csrf_exempt
@invalid_data
@require_http_methods("GET")
def get_mentees(record, user):        #get mentees of a given user
    """
    Get Users being mentored by a particular User
    """
    userid = user + 0   #to enforce user id given being an integer
    projects = list(Project_User.objects.filter(User_id = userid, IsMentor = True).values_list('Project_id', flat = True))
    mentees = set(Project_User.objects.filter(Project_id__in=projects, IsMentor=False).values_list('User_id', flat=True))
    # mentees = list(set(mentees))
    mentees = sorted(list(mentees))
    names = list(User.objects.filter(id__in=mentees).order_by('id').values_list('Name', flat = True))
    mentees = {"ids": mentees, "names": names}
    mentees = json.dumps(mentees)
    return HttpResponse(mentees, content_type = "text/json")


@csrf_exempt
@invalid_data
@require_http_methods("GET")
def get_projects_mentored_by_user(record, user):
    """
    List Projects Mentored by a User
    """
    userid = user + 0
    projects = set(Project_User.objects.filter(User_id = userid, IsMentor = True).values_list('Project_id', flat = True))
    projects = sorted(list(projects))
    names = list(Project.objects.filter(id__in=projects).order_by('id').values_list('Name', flat=True))
    projects = json.dumps({"ids": projects, "project_names": names})
    return HttpResponse(projects, content_type = "text/json")


@csrf_exempt
@invalid_data
@require_http_methods("GET")
def get_users_mentors(record, project):    #get users/mentor of a project
    """
    Get Mentors and Users of a Project
    """
    project_id = project + 0
    users = set(Project_User.objects.filter(Project_id = project_id, IsMentor = False).values_list('User_id', flat = True))
    mentors = set(Project_User.objects.filter(Project_id = project_id, IsMentor = True).values_list('User_id', flat = True))
    users = sorted(list(users))
    mentors = sorted(list(mentors))
    user_names = list(User.objects.filter(id__in=users).order_by('id').values_list('Name', flat=True))
    mentor_names = list(User.objects.filter(id__in=mentors).order_by('id').values_list('Name', flat=True))
    final_dict = json.dumps({"users": users, "mentors": mentors, "user_names": user_names, "mentor_names": mentor_names})
    return HttpResponse(final_dict, content_type = "text/json")


@csrf_exempt
@invalid_data
@require_http_methods("GET")
def get_mentors(record, project):
    """
    Get Mentors of a Project
    """
    project_id = project + 0
    mentors = set(Project_User.objects.filter(Project_id=project_id, IsMentor=True).values_list('User_id', flat=True))
    mentors = sorted(list(mentors))
    mentor_names = list(User.objects.filter(id__in=mentors).order_by('id').values_list('Name', flat=True))
    final_dict = json.dumps({"mentor_ids": mentors, "mentor_names": mentor_names})
    return HttpResponse(final_dict, content_type="text/json")

@csrf_exempt
@invalid_data
@require_http_methods("GET")
def get_all_projects(record):
    """
    Get all projects with their users and mentors
    """
    projects = list(Project.objects.filter().values('id', 'Name'))
    ###################
    for project in projects:
        project_id = project["id"]
        users = set(
            Project_User.objects.filter(Project_id=project_id, IsMentor=False).values_list('User_id', flat=True))
        mentors = set(
            Project_User.objects.filter(Project_id=project_id, IsMentor=True).values_list('User_id', flat=True))
        users = sorted(list(users))
        mentors = sorted(list(mentors))
        user_names = list(User.objects.filter(id__in=users).order_by('id').values_list('Name', flat=True))
        mentor_names = list(User.objects.filter(id__in=mentors).order_by('id').values_list('Name', flat=True))
        project['users'] = list(zip(users, user_names))
        project['mentors'] = list(zip(mentors, mentor_names))
    ####################
    final_dict = json.dumps({"info": projects})
    return HttpResponse(final_dict, content_type="text/json")