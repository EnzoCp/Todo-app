from django.db import models


# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=64)
    sub_title = models.CharField(max_length=32, blank=True, null=True)
    content = models.TextField(max_length=512)

    def __str__(self):
        return f"{self.title}"
