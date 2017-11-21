from django.contrib import admin
from .models import Category, Cake1
from django.utils.safestring import mark_safe
from form_utils.widgets import ImageWidget
from django.db import models

# Register your models here.

admin.site.register(Category)
# admin.site.register(Cake1)
admin.site.site_header = "后台管理"


class Cake1Admin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')
    formfield_overrides = {models.ImageField: {'widget': ImageWidget}}
    list_filter = ('category_id',)
    search_fields = ('name',)
    # fieldsets = [
    #     (None, {'fields': ['name', 'price', 'discount_price', 'img', 'desc', 'pub_time', 'category_id']}),
    # ]
    # list_per_page = 5



    # readonly_fields = ('img_data',)

    # def img_data(self, obj):
    #     return mark_safe(u'<img src="%s" width="50px" height="50px" />' % obj.img.url)
    #
    # img_data.short_description = "图片预览"


admin.site.register(Cake1, Cake1Admin)
