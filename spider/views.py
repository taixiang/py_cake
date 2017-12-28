from django.shortcuts import render
from spider.models import learn

# Create your views here.

def enList(request):
    list = learn.objects.all()