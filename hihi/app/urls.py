from django.urls import path

from .views import NormanPage, uploadFile

urlpatterns = [
    path('NormanPage/', NormanPage),
    path('upload/', uploadFile),
]
