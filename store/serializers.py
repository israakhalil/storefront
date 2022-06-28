import collections
from dataclasses import field
from pyexpat import model
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from decimal import Decimal
from store.models import Product,Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Collection
        fields=['id','title','product_count']

    product_count=serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        # field='__all__' bad practice 
        fields=['id','title','description','slug','inventory','unit_price','price_with_tax','collection']

    price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self,product:Product):
        return product.unit_price* Decimal(1.1)
    
    # def create(self, validated_data):
    #     product= Product(**validated_data)
    #     product.other=1
    #     product.save()
    #     return product
    
    # def update(self, instance, validated_data):
    #     instance.unit_price=validated_data.get('unit_price')
    #     instance.save()
    #     return instance














# class CollectionSerializer(serializers.Serializer):
#     id=serializers.IntegerField()
#     title=serializers.CharField(max_length=255)

# class ProductSerializer(serializers.Serializer):
#     id= serializers.IntegerField()
#     title=serializers.CharField(max_length=255)
#     # unit_price=serializers.DecimalField(max_digits=6, decimal_places=2)
#     price=serializers.DecimalField(max_digits=6, decimal_places=2,source='unit_price')
#     price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')
#     collection=serializers.PrimaryKeyRelatedField(
#         queryset= Collection.objects.all(),
#         # source='collection'
#     )
#     # collection2=serializers.StringRelatedField(source='collection')
#     # collection3=CollectionSerializer(source='collection')
#     # collection4=serializers.HyperlinkedRelatedField(
#     #     queryset=Collection.objects.all(),
#     #     view_name='collection_detail',
#     #     source='collection'
        
#     # )

#     def calculate_tax(self,product:Product):
#         return product.unit_price* Decimal(1.1)


