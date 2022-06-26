from turtle import title
from django.shortcuts import get_object_or_404
from store.models import Collection, Product
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

@api_view()
def product_list(request):
    # queryset=Product.objects.all()
    queryset=Product.objects.select_related('collection').all()
    serializer=ProductSerializer(queryset,many=True,context={'request': request})
    return Response(serializer.data)

@api_view()
def product_detail(request,id):
    # try:
    #     product=Product.objects.get(pk=id)
    #     serializer=ProductSerializer(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
        product=get_object_or_404(Product, pk=id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)    

@api_view()
def collection_detail(request,pk):
    return Response('ok')

