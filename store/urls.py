from django.urls import include, path
from rest_framework import routers
from . import views

# class Based View =ViewSet
router=routers.SimpleRouter()
router.register('products',views.ProductViewSet)
router.register('collections',views.CollectionViewSet)
urlpatterns = router.urls
# urlpatterns=[
#     path('', include(router.urls)),
#     path()
# ]


# router=routers.DefaultRouter
#لو حطيت باخر  الرابط json in browser
# بقدر احصل على الملف جيسون
# بيعطيني روابط للراوت الرئيسية الي عندي 




# #class based View = APIView, Mixin,GenericView
# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetails.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collection_detail')
# ]

# # function based view
# urlpatterns = [
#     path('products/', views.product_list),
#     path('products/<int:id>/', views.product_detail),
# ]