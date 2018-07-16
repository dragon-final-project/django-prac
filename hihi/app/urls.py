from django.urls import path

from .views import index, NormanPage, IndexView, uploadFile

urlpatterns = [
    path('', IndexView.as_view()),
    path('NormanPage/', NormanPage),
    path('upload/', uploadFile),
]
