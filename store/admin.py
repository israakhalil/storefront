
from urllib.parse import urlencode
from django.contrib import admin,messages
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html 
from django.db.models.query import QuerySet
from . import models

# Register your models here.

class inventoryFilter(admin.SimpleListFilter):
    title="inventory"
    parameter_name="inventory"
    def lookups(self, request, model_admin):
        return [('<10', 'low')] 

    def queryset(self, request, queryset: QuerySet):
        if self.value() =='<10':
            return queryset.filter(inventory__lt=10)




@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display=['title','product_count']
    search_fields=['title']
    
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
    prepopulated_fields={
        'slug':['title']
    }
    autocomplete_fields= ['collection']
    actions= ['clear_inventory']
    list_display = ['title','unit_price','inventory_status','collection']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related= ['collection']
    list_filter= ['collection','last_update',inventoryFilter]
    search_fields =['title']

    
    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10 :
            return 'low'
        return 'ok'
    
    @admin.action(description="clear inventory")
    def clear_inventory(self,request,queryset):
        updated_count=queryset.update(inventory=0)
        self.message_user(request,
        f'{updated_count} products were successfully update',
        messages.ERROR)

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


    
class OrderItemInline(admin.TabularInline):
    autocomplete_fields =['product']
    model=models.OrderItem
    extra=0
    min_num=1

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields= ['customer']
    list_display=['id','customer','placed_at','payment_status']
    list_editable=['payment_status']
    list_per_page = 10
    inlines=[OrderItemInline]
    # list_select_related=['customer']


