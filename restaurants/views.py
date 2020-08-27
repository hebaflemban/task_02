from django.shortcuts import render

def home(request):

    context = {
        'msg' : 'Hello World!! +_-'

    }

    return render(request, 'home.html', context)
