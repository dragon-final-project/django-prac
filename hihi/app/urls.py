from django.urls import path

from .views import NormanPage, uploadFile, PicListView

urlpatterns = [
    path('NormanPage/', NormanPage),
    path('upload/', uploadFile),
    path('pic_list/', PicListView.as_view())
]
