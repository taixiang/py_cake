from django.db import models

# Create your models here.


from django.db import models


class Poems(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author_id = models.IntegerField()
    dynasty = models.CharField(max_length=10, blank=True, null=True)
    author = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'poems'


class PoemsAuthor(models.Model):
    name = models.CharField(max_length=150)
    intro_l = models.TextField(blank=True, null=True)
    intro_s = models.TextField()
    dynasty = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poems_author'
