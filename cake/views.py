from django.shortcuts import render
from .models import Category, Cake1
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.core import serializers
from rest_framework import viewsets, generics
from cake.serializer import CategorySerializer, CakeSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


# Create your views here.分页


def category(request):
    categorys = Category.objects.all()
    allcake = Cake1.objects.all()
    # t = Category.objects.get(id=1)
    # cake = categorys.cake1_set.all()
    # w = get_list_or_404(Cake1, category_id=categorys[0].id)
    print(222222)
    paginator = Paginator(allcake, 1)
    page = request.GET.get('page')
    # if page:
    #     cake_list = paginator.page(page).object_list
    # else:
    #     cake_list = paginator.page(1).object_list


    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        print("==================")
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    data = serializers.serialize("json", allcake)

    print(JsonResponse(data, safe=False))
    return render(request, "cake/cake.html", {"categorys": categorys, "allcake": customer})
    # return JsonResponse(data, safe=False)


def category_json(request):
    categorys = Category.objects.all()
    allcake = Cake1.objects.all()
    # t = Category.objects.get(id=1)
    # cake = categorys.cake1_set.all()
    # w = get_list_or_404(Cake1, category_id=categorys[0].id)
    print(222222)
    paginator = Paginator(allcake, 1)
    page = request.GET.get('page')
    # if page:
    #     cake_list = paginator.page(page).object_list
    # else:
    #     cake_list = paginator.page(1).object_list

    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    customer.next_ = "11111"

    data = serializers.serialize("json", customer)
    data = "{ \"data\":" + data + ",\"page\":" + page + " }"
    print(data)
    print("===================================")
    # return render(request, "cake/cake.html", {"categorys": categorys, "allcake": customer})
    return JsonResponse(data, safe=False)


def cakeList(request, category_id):
    categorys = Category.objects.all()
    allcake = Cake1.objects.filter(category_id=category_id)
    paginator = Paginator(allcake, 5)
    page = request.GET.get('page')
    # if page:
    #     cake_list = paginator.page(page).object_list
    # else:
    #     cake_list = paginator.page(1).object_list

    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    print(33333)
    print(allcake)
    return render(request, "cake/cake.html", {"categorys": categorys, "allcake": customer, "cake_id": int(category_id)})


def cakeDetail(request, cake_id):
    cake_detail = Cake1.objects.get(id=cake_id)
    categorys = Category.objects.all()
    return render(request, "cake/detail.html", {"categorys": categorys, "detail": cake_detail})


def page_not_find(request):
    return render(request, "cake/404.html")


# 后台登录
def cakeLogin(request):
    if request.POST:
        # name = request.POST['user_name']
        # print(name)
        print(22222)
    return render(request, "cake/login.html")


def cakeAdminList(request):
    return render(request, "cake/adminlist.html")


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CakeListViewSet(viewsets.ModelViewSet):
    queryset = Cake1.objects.all()
    serializer_class = CakeSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CakeApiView(generics.ListAPIView):
    serializer_class = CakeSerializer
    queryset = Cake1.objects.all()
