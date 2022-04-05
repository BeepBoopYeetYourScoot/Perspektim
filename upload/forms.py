from django import forms
from .utils import validate_size


class UploadFileForm(forms.Form):
    author = forms.CharField(max_length=255, label='Автор')
    file = forms.FileField(validators=[validate_size], label='Файл')
