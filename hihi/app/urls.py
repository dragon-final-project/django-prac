from django.urls import path

from .views import index, NormanPage, IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('NormanPage/', NormanPage)
]
