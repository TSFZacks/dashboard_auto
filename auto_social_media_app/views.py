from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return render(request, 'pages/index.html')
def facebook_views(request):
    return render(request, 'pages/facebook_page.html')