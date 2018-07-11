from django.shortcuts import render

# Create your views here.
def secreat(request):
    my_dict = {
        'secreats': ['secreat1', 'secreat2', 'secreat3'],
        'answer': 'no secreat!'
    }
    return render(request, 'secreat.html', context=my_dict)
