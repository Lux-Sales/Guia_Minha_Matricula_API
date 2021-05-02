from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import PROTECT

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)