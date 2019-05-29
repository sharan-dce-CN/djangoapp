# Create your models here.

from django.db import models

class User(models.Model):
    Name = models.CharField(max_length = 50)
    def __str__(self):
        return self.Name

class Project(models.Model):
    Name = models.CharField(max_length = 500)
    many_to_many_mapping_proj_user = models.ManyToManyField(User, through = 'Project_User')
    def __str__(self):
        return self.Name

class Project_User(models.Model):
    Project_id = models.ForeignKey(Project, on_delete = models.CASCADE)
    User_id = models.ForeignKey(User, on_delete = models.CASCADE)
    IsMentor = models.BooleanField(default = False)

