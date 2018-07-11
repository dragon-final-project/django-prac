from django.urls import path

from .views import index , NormanPage

urlpatterns = [
    path('', index),
    path('NormanPage/', NormanPage)
]

# URL/app/show/
