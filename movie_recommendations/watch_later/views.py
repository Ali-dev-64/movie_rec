from django.shortcuts import render


watch_later=[1,2]
# Create your views here.
def list(request):
    return render(request, "watch_later/index.html",{
        "list":watch_later
    })