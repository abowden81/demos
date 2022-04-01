from rest_framework import serializers

from .models import Product
#serialize product data for use in autocomplete field
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'