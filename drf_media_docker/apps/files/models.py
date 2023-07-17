from django.db import models

from project_common.models import BaseModel


class File(BaseModel):
    title = models.CharField(max_length=50, blank=True, default='')
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title or self.file.name
