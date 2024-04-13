from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "D:/ALI/movie_rec/movie_recommendations/home/templates/home/index.html")
