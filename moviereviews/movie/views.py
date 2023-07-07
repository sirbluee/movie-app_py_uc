from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
def mypagefunction(request):
    return HttpResponse('<h1>Welcome to my page</h1>')

def contactfunction(request):
    return render(request, 'contact_page.html')

def movDetailfunction(request):

    best_movie = { 'mov_title': 'Transformer-Dark of the moon',
                    'author':'Ehen Kruer',
                    'release_year': '2011',
                    'language':'English'
                }

    return render(request, 'detail_page.html', best_movie)



