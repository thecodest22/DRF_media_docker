from django.db import models

from project_common.models import BaseModel


class Video(BaseModel):
    title = models.CharField(max_length=50, default='')
    url = models.URLField()

    def __str__(self):
        return self.title
