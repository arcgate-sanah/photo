from django.shortcuts import render
from django.http import HttpResponse


def index(request):
 
    return render(request, 'photos/index.html')

def new(request,photos_id):
    album = photos.objects.get(pk='photos_id')
    return render(request, 'photos/index.html',album)




