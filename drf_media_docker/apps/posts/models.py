from django.db import models

from project_common.models import BaseModel, BaseImage


class Post(BaseModel):
    title = models.CharField(max_length=255, blank=True, default='')
    body = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title


class PostImage(BaseImage):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
