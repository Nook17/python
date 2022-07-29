from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('media-example/', views.mediaExample, name='media-example'),
    path('media-example-django/', views.mediaExampleDjango, name='media-example-django'),
    path('media-images/', views.mediaImages, name='media-images'),
    path('media-model/', views.mediaModel, name='media-model'),
    path('media-model-form/', views.mediaModelForm, name='media-model-form'),
]

# warunkowe dodanie mapowania URL z opcją MEDIA_URL na widok static,
# który będzie zwracał plik z katalogu ustawionego w opcji MEDIA_ROOT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)