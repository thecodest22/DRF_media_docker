from django.contrib import admin

from .models import Post, PostImage
from .forms import PostAdminForm


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
