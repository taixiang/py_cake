from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Category, Cake1
# Create your views here.


def category(request):
    categorys = Category.objects.all()
    # t = Category.objects.get(id=1)
    # q = Cake1.objects.filter(category_id=categorys[0].id)
    # cake = categorys.cake1_set.all()
    # w = get_list_or_404(Cake1, category_id=categorys[0].id)
    print(categorys)
    return render(request, "cake/cake.html", {"categorys": categorys})