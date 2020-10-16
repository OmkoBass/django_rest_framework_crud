from django.db import models


class Todo(models.Model):
    todo = models.CharField(max_length=128)
    completed = models.BooleanField(default=False)
