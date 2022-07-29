from django.shortcuts import render
from django.conf import settings
from .forms import UploadForm, UploadImagesForm, UploadImageModel, UploadImageModelForm
from .models import ExampleModel
from PIL import Image
import os


def index(request):
    return render(request, 'index.html')


def mediaExample(request):
    if request.method == 'POST':
        save_path = os.path.join(settings.MEDIA_ROOT, request.FILES["file_upload"].name)
        with open(save_path, "wb") as output_file:
            for chunk in request.FILES["file_upload"].chunks():
                output_file.write(chunk)
    return render(request, 'media-example.html')


def mediaExampleDjango(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            save_path = os.path.join(settings.MEDIA_ROOT, request.FILES["file_upload"].name)
            with open(save_path, "wb") as output_file:
                for chunk in form.cleaned_data["file_upload"].chunks():
                    output_file.write(chunk)
    else:
        form = UploadForm()
    context = {"form": form}
    return render(request, 'media-example-django.html', context)


def mediaImages(request):
    if request.method == "POST":
        form = UploadImagesForm(request.POST, request.FILES)
        if form.is_valid():
            save_path = os.path.join(settings.MEDIA_ROOT, request.FILES["file_image_upload"].name)
            image = Image.open(form.cleaned_data["file_image_upload"])
            image.thumbnail((200, 200))
            image.save(save_path)
    else:
        form = UploadImagesForm()
    context = {"form": form}
    return render(request, 'media-images.html', context)


def mediaModel(request):
    instance = None
    if request.method == 'POST':
        form = UploadImageModel(request.POST, request.FILES)
        if form.is_valid():
            instance = ExampleModel()
            instance.image_field = form.cleaned_data["image_upload"]
            instance.file_field = form.cleaned_data["file_upload"]
            instance.save()
    else:
            form = UploadImageModel()
    context = {"form": form, "instance": instance}
    return render(request, 'media-model.html', context)


def mediaModelForm(request):
    instance = None
    if request.method == 'POST':
        form = UploadImageModelForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
    else:
            form = UploadImageModelForm()
    context = {"form": form, "instance": instance}
    return render(request, 'media-model-form.html', context)
