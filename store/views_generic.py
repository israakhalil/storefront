from django.http import QueryDict
from django.shortcuts import get_object_or_404
from store.models import Collection, Product
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import status
from .models import Product
from django.db.models import Count
from .serializers import CollectionSerializer, ProductSerializer
# Create your views here.

class ProductList(ListCreateAPIView):
    queryset=Product.objects.select_related('collection').all()
    serializer_class=ProductSerializer
    def get_serializer_context(self):
        return {'request': self.request}

#     لمن يكون عندي لوجيك او كونديشن معين بدي ابنيه بستخدم الميثود هدول ..
#    لكن لو كان الاشي بسيط بستخدم البارميترز الي فوق مباشرة
    # def get_queryset(self):
    #     return Product.objects.select_related('collection').all()
    
    # def get_serializer_class(self):
    #     return ProductSerializer

class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def delete(self, request,pk):
        product=get_object_or_404(Product, pk=pk)
        if product.orderitem.count() >0:
            return Response({"error":" product have associated with order item"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CollectionList(ListCreateAPIView):
    queryset=Collection.objects.annotate(product_count=Count('product')).all()
    serializer_class=CollectionSerializer
  


class CollectionDetail(RetrieveUpdateDestroyAPIView):
    queryset=Collection.objects.annotate(product_count=Count('product'))
    serializer_class=CollectionSerializer

    def delete(self, request,pk):
        collection=get_object_or_404(Collection, pk=pk)
        if collection.product_set.count() >0:
            return Response({"error":" collection have associated with product item"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)        