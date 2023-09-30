from django.db import models


class Student(models.Model):
    tg_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    attendance = models.SmallIntegerField(default=0)
    points = models.SmallIntegerField(default=0)
