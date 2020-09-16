from django.shortcuts import render

def home(request):
    data = {}
    return render(request,
                  'home/index.jhtml',
                  data)