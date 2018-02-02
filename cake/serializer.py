from cake.models import Category, Cake1
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    pub_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Category
        fields = ('id', 'category', 'pub_time', 'order')


class CakeSerializer(serializers.HyperlinkedModelSerializer):
    pub_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    category_id = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cake1
        fields = ('id', 'name', 'price', 'discount_price', 'desc', 'label', 'pub_time', 'category_id')
