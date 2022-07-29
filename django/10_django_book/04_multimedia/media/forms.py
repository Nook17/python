from django import forms
from .models import ExampleModel


class UploadForm(forms.Form):
    file_upload = forms.FileField()


class UploadImagesForm(forms.Form):
    file_image_upload = forms.ImageField()


class UploadImageModel(forms.Form):
    image_upload = forms.ImageField()
    file_upload = forms.FileField()


class UploadImageModelForm(forms.ModelForm):
    class Meta:
        model = ExampleModel
        fields = "__all__"
