from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse
from .models import UploadPic

def NormanPage(request):
    my_dict = {
        'name': 'NormanPage',
        'Detail': 'Cool'
    }
    return render(request, 'NormanPage.html', context=my_dict)


def uploadFile(request):
    if request.method == 'POST':
        data = request.FILES['image_file']

        # save to local pic
        with open('static/save_img/' + str(data), 'wb') as jpg_f:
            for chunk in data.chunks():
                jpg_f.write(chunk)
        # save to model
        UploadPic.objects.create(user="smalldragon",
        pic_name=str(data), pic_desc="no")

        return HttpResponse('<div>Upload Success!!</div><img src="/static/save_img/' + str(data) + '" />')
    else:
        return render(request, 'upload.html')

class PicListView(ListView):
    model = UploadPic
    template_name = 'pic_list.html'
    context_object_name = 'pics'

# 3 4 1 0 5 17
