from cake.models import Category, Cake1
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    pub_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Category
        fields = ('id', 'category', 'pub_time', 'order')
