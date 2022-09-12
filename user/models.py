from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class uSleep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, default=0)
    sleepStart = models.CharField(max_length=100, null=False, blank=False, default="Null")
    sleepEnd = models.CharField(max_length=100, null=False, blank=False, default="Null")
    currentDate = models.CharField(max_length=100, null=False, blank=False, default="Null")
    duration = models.CharField(max_length=100, null=True, blank=True, default="Null")
    # , auto_now=False

    def __str__(self):
        return self.user.username