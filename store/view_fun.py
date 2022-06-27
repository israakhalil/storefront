from django.shortcuts import get_object_or_404
from store.models import Collection, Product
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
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


@api_view(['GET','POST'])
def collection_list(request):
    if request.method=='GET':
        queryset= Collection.objects.annotate(product_count=Count('product')).all()
        serializer=CollectionSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def collection_detail(request,id):
    collection=get_object_or_404(Collection.objects.annotate(product_count=Count('product')), pk=id)
    if request.method=='GET':
        serializer=CollectionSerializer(collection)
        return Response(serializer.data)
    if request.method=='PUT':
        serializer=CollectionSerializer(collection,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method =='DELETE' :
        # if product.orderitem_set.count() >0:
        if collection.product_set.count() >0:
            return Response({"error":" collection have associated with product item"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        











# @api_view(['GET','POST'])
# def product_list(request):
#     if request.method=='GET':
#     # queryset=Product.objects.all()
#         queryset=Product.objects.select_related('collection').all()
#         serializer=ProductSerializer(queryset,many=True,context={'request': request})
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.validated_data
#             return Response('ok')
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view()
# def product_detail(request,id):
#     try:
#         product=Product.objects.get(pk=id)
#         serializer=ProductSerializer(product)
#         return Response(serializer.data)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
