from cake.models import Category, Cake1
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    pub_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Category
        fields = ('id', 'category', 'pub_time', 'order')


class CakeSerializer(serializers.ModelSerializer):
    # sub = SecondeSerializer(many=True)

    pub_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    category_id = serializers.StringRelatedField(many=True)

    class Meta:
        model = Cake1
        fields = ('id', 'name', 'price', 'discount_price', 'desc', 'label', 'pub_time', 'category_id')


class SecondeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category',)
        list_serializer_class = FilterSerializer


class FilterSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        return super(FilterSerializer, self).to_representation(data)
