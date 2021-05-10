from django.db import models
from django.db.models.deletion import PROTECT
from users.models import User

class Teacher(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Comment(models.Model):
    comment = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=PROTECT)
    subject = models.ForeignKey(Subject, on_delete=PROTECT)
    user = models.ForeignKey(User, on_delete=PROTECT)
