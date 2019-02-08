from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Category
from .serializers import CategorySerializer, ProductCategorySerializer

class List(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)

class productsCategory(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = (AllowAny,)
