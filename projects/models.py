from django.db import models
from django.conf import settings


class Project(models.Model):
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
    )
    name = models.CharField("name", max_length=200)
    create_date = models.DateTimeField("create date")
    last_edit_date = models.DateTimeField("last edit date")

    def __str__(self):
        return self.name


class Measurement(models.Model):
    event = models.CharField("event", max_length=100)
    name = models.CharField("name", max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event}/{self.name}"
