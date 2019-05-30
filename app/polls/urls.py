from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),       #root page
    path('user', views.create_user),      #create user
    path('project', views.create_project),  #create project
    path('project/assign', views.assign_project_to_users),  #assign project to users
    path('user/assign-as-mentor', views.assign_mentor),        #assign one user as mentor to a project
    path('project/assign-users', views.assign_users_to_project),      #assign users to a project
    path('user/<int:user>/mentees', views.get_mentees),         #get mentees of a given user
    path('user/<int:user>/projects-mentoring', views.get_projects_mentored_by_user),    #get projects user is mentoring
    path('project/<int:project>/get-users-mentors', views.get_users_mentors),    #get users/mentor of a project
    path('project/<int:project>/get-mentors', views.get_mentors),     #get mentors of a project
    path('project/get-all-projects', views.get_all_projects),     #get all projects with users and mentors
    path('project/compare-logs', views.compare) #for checking whether changes have been made
]