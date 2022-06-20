from turtle import title
from django.shortcuts import render
from store.models import Collection, Product

# Create your views here.

def say_hello(request):
    # query_set =Product.objects.filter(unit_price__range=(20,30))
    query_set =Product.objects.values('id','title','collection__title')
    return render(request,'hello.html' ,{'name':'Israa', 'products':list(query_set)})
