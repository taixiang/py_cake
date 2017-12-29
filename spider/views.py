from django.shortcuts import render
from spider.models import learn
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers


# Create your views here.

def enList(request):
    enList = learn.objects.all()
    paginator = Paginator(enList, 10)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    return render(request, "spider/english.html", {"enList": customer})


def enList_json(request):
    enList = learn.objects.all()
    paginator = Paginator(enList, 10)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    data = serializers.serialize("json", customer)
    data = "{ \"data\":" + data + ",\"page\":" + page + " }"
    return JsonResponse(data, safe=False)


def enDetail(request, enid):
    detail = learn.objects.get(id=enid)
    return render(request, "spider/detail.html", {"detail": detail})
