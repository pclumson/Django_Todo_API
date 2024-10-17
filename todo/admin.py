from django.contrib import admin
from django.contrib.auth.models import Group, User
from todo.models import Task

# Register your models here.
admin.site.register(Task)
