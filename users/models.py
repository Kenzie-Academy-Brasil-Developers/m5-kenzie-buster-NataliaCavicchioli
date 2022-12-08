from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)
    is_employee = models.BooleanField(null=True, blank=True, default=False)
