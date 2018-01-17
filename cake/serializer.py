from cake.models import Category, Cake1
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('category', 'pub_time', 'order')
