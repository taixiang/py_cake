from django.contrib import admin
from .models import Poems, PoemsAuthor

# Register your models here.
admin.site.register(Poems)
admin.site.register(PoemsAuthor)
