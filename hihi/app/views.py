from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Person

# Create your views here.
def index(request):
    my_dict = {
        'names': ['Jackson', 'Jason', 'Lisa'],
        'birthday': '1997/06/17'
    }
    return render(request, 'index.html', context=my_dict)

class IndexView(View):
    def get(self, request):
        my_dict = {
            'names': ['Jackson', 'Jason', 'Lisa'],
            'birthday': '1997/06/17'
        }
        return render(request, 'index.html', context=my_dict)

def NormanPage(request):
    my_dict = {
        'name': 'NormanPage',
        'Detail': 'Cool'
    }
    return render(request, 'NormanPage.html', context=my_dict)


def uploadFile(request):
    if request.method == 'POST':
        data = request.FILES['image_file']

        with open('static/save_img/' + str(data), 'wb') as jpg_f:
            for chunk in data.chunks():
                jpg_f.write(chunk)
        return HttpResponse('<div>Upload Success!!</div><img src="/static/save_img/' + str(data) + '" />')
    else:
        return render(request, 'upload.html')
