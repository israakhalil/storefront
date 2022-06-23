from urllib.parse import urlencode
from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html 
from . import models

# Register your models here.

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display=['title','product_count']
    
    @admin.display(ordering='product_count')
    def product_count(self,collection):
        url=(
            reverse('admin:store_product_changelist' )
            + '?' 
            + urlencode({
            'collection__id':str(collection.id)
        }))
        return format_html('<a href="{}">{}</a>',url,collection.product_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count= Count('product')
        )
    
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price','inventory_status','collection']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related= ['collection']
    list_filter= ['collection','last_update']

    
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10 :
            return 'low'
        return 'ok'

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =['first_name','last_name','membership','orders_count']
    list_editable = ['membership']
    ordering= ['first_name','last_name']
    list_per_page= 10
    search_fields=['first_name__istartswith','last_name__istartswith']
  
    @admin.display(ordering='orders_count')
    def orders_count(self,customer):
        url=(
            reverse('admin:store_order_changelist' )
            + '?' 
            + urlencode({
            'customer__id':str(customer.id)
        }))
        return format_html('<a href="{}">{}</a>',url,customer.orders_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            orders_count= Count('order')
        )


    

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','customer','placed_at','payment_status']
    list_editable=['payment_status']
    list_per_page = 10
    # list_select_related=['customer']


