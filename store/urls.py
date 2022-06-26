from unicodedata import name
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('products/', views.product_list),
    path('products/<int:id>/', views.product_detail),
    path('collection/<int:pk>/', views.collection_detail, name='collection_detail')
]

# Django RestFarmework
# https://www.django-rest-framework.org/
# https://www.django-rest-framework.org/api-guide/fields/
