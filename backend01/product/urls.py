from django.urls import path
from .views import ProductAPI , PurchaseProduct

urlpatterns = [
    path('Products/', ProductAPI.as_view()),
    path('purchase/', PurchaseProduct.as_view())
]