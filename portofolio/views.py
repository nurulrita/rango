from django.shortcuts import render

def index(request):
    context_dict = {}
    return render (request, 'portofolio/index.html', context_dict)
