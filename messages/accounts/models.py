from django.db import models
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
# Create your models here.
class Users(User,PermissionRequiredMixin,models.Model):

    def __str__(self):
        return self.username
