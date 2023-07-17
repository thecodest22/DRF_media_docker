from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Post


class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = '__all__'
