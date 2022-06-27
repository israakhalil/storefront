from unicodedata import name
from django.urls import path
from . import views

# URLConf
urlpatterns = [
    # path('products/', views.product_list),
    # path('products/<int:id>/', views.product_detail),
    path('products/', views.ProductList.as_view()),
    path('products/<int:id>/', views.ProductDetails.as_view()),
    path('collections/', views.collection_list),
    path('collections/<int:id>/', views.collection_detail, name='collection_detail')
]