from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {
        'names': ['Jackson', 'Jason', 'Lisa'],
        'birthday': '1997/06/17'
    }
    return render(request, 'index.html', context=my_dict)
