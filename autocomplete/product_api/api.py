from rest_framework import generics
from rest_framework import filters
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

#import data and serializer for use in autocomplete
from .serializers import ProductSerializer
from .models import Product

class ProductApi(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('sku','name')