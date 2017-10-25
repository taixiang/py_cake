from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField("问题", max_length=200)
    pub_date = models.DateTimeField("发布时间")
    pub_who = models.CharField("谁发布的", max_length=200, default="0")

    def __str__(self):
        return self.question_text
