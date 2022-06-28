from django.shortcuts import get_object_or_404
from store.models import Collection, Product
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin
from rest_framework import status
from .models import Product
from django.db.models import Count
from .serializers import CollectionSerializer, ProductSerializer
# Create your views here.

class ProductList(APIView):
    def get(self, request):
        queryset=Product.objects.select_related('collection').all()
        serializer=ProductSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data,status=status.HTTP_201_CREATED)


class ProductDetails(APIView):
    def get(self, request,id):
        product=get_object_or_404(Product, pk=id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)
        
    def put(self, request,id):
        product=get_object_or_404(Product, pk=id)
        serializer=ProductSerializer(product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request,id):
        product=get_object_or_404(Product, pk=id)
        if product.orderitem.count() >0:
            return Response({"error":" product have associated with order item"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
