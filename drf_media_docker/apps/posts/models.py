from django.db import models

from project_common.models import BaseModel


class Post(BaseModel):
    title = models.CharField(max_length=255, blank=True, default='')
    body = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title
