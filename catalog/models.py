from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Redactor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Redactor"
        verbose_name_plural = "Redactors"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField(null=True)
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    redactors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="newspapers")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title
