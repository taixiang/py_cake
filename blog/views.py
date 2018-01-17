from django.shortcuts import render


# Create your views here.

def appUrl(request):
    return render(request, "blog/test.html")
