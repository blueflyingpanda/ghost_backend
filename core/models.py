from django.db import models


class Student(models.Model):
    tg_id = models.CharField()
    name = models.CharField()
    attendance = models.SmallIntegerField(default=0)
    points = models.SmallIntegerField(default=0)
