from django.db import models


# Create your models here.

class article(models.Model):
    title = models.CharField("标题", max_length=200, blank=True)
    content = models.TextField("内容", blank=True)
    author = models.CharField("作者", max_length=100, blank=True)

    def __str__(self):
        return self.title


class learn(models.Model):
    title = models.CharField("标题", max_length=200, blank=True)
    time = models.DateField("时间", blank=True)
    content = models.TextField("内容", blank=True)
    url = models.CharField("链接", max_length=200, blank=True)
    audioUrl = models.CharField("听力", max_length=200, blank=True)

    class Meta:
        ordering = ("-time",)

    def __str__(self):
        return self.time.strftime("%Y-%m-%d")
