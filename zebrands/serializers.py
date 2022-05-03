from rest_framework import serializers
from zebrands.models import Brand, Product


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_brand_name(self, obj):
        return obj.brand_id.title
