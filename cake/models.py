from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


# Create your models here.


class Category(models.Model):
    category = models.CharField("类别", max_length=50)
    pub_time = models.DateTimeField("时间", default=timezone.now)
    order = models.IntegerField("排序", default=0)

    class Meta:
        ordering = ("pub_time",)
        verbose_name = "分类"
        verbose_name_plural = "分类"
        # app_label = u"分类"

    def __str__(self):
        return self.category


class Cake1(models.Model):
    name = models.CharField("名字", max_length=200)
    price = models.DecimalField("价格", max_digits=6, decimal_places=2)
    discount_price = models.DecimalField("优惠", max_digits=6, decimal_places=2)
    img = models.ImageField("图片", upload_to="photos/%Y/%m/%d")
    desc = models.CharField("描述", max_length=500)
    label = models.CharField("标签", max_length=400)
    cake_desc = models.TextField("文本", null=True, blank=True, help_text="z这是文本信息")
    order = models.IntegerField("权重", default=0)
    pub_time = models.DateTimeField("时间", default=timezone.now)
    category_id = models.ManyToManyField("Category", related_name="cake_post", verbose_name="类别", blank=True)

    class Meta:
        ordering = ("pub_time",)
        verbose_name = "蛋糕详情"
        verbose_name_plural = "蛋糕详情"

    # def img_data(self, obj):
    #     return mark_safe(u'<img src="%s" width="50px" height="50px" />' % obj.image.url)
    #
    # img_data.short_decription = "图片预览222"

    def image(self):
        return '<img src="/static/img/%s" width="50px" height="50px" />'% self.img

    image.allow_tags = True

    def __str__(self):
        return self.name