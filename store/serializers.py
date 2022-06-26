import collections
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from decimal import Decimal
from store.models import Product,Collection

class CollectionSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=255)

class ProductSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    title=serializers.CharField(max_length=255)
    # unit_price=serializers.DecimalField(max_digits=6, decimal_places=2)
    price=serializers.DecimalField(max_digits=6, decimal_places=2,source='unit_price')
    price_with_tax=serializers.SerializerMethodField(method_name='calculate_tax')
    collection1=serializers.PrimaryKeyRelatedField(
        queryset= Collection.objects.all(),
        source='collection'
    )
    collection2=serializers.StringRelatedField(source='collection')
    collection3=CollectionSerializer(source='collection')
    collection4=serializers.HyperlinkedRelatedField(
        queryset=Collection.objects.all(),
        view_name='collection_detail',
        source='collection'
        
    )

    def calculate_tax(self,product:Product):
        return product.unit_price* Decimal(1.1)