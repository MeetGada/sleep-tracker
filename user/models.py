from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class uSleep(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, default=0)
    sleepStart = models.DateTimeField(null=False, blank=False, auto_now=False, default=timezone.now())
    sleepEnd = models.DateTimeField(null=False, blank=False, auto_now=False, default=timezone.now())
    duration = models.DurationField(null=True, blank=True)
    # , auto_now=False

    def __str__(self):
        return self.user.username