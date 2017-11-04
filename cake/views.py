from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, Cake1


# Create your views here.


def category(request):
    categorys = Category.objects.all()
    allcake = Cake1.objects.all()
    # t = Category.objects.get(id=1)
    # cake = categorys.cake1_set.all()
    # w = get_list_or_404(Cake1, category_id=categorys[0].id)
    print(222222)

    return render(request, "cake/cake.html", {"categorys": categorys, "allcake": allcake})


def cakeList(request, category_id):
    categorys = Category.objects.all()
    allcake = Cake1.objects.filter(category_id=category_id)
    print(111111)
    print(type(category_id))
    return render(request, "cake/cake.html", {"categorys": categorys, "allcake": allcake, "cate_id": int(category_id)})


def cakeDetail(request, cake_id):
    cake_detail = Cake1.objects.get(id=cake_id)

    print(cake_detail)
    return render(request, "cake/detail.html", {"detail": cake_detail})
