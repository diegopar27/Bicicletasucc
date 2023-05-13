from rest_framework.routers import DefaultRouter
from .views import ProductModelViewSet


router_Product = DefaultRouter()

router_Product.register(prefix='Product', basename='Product', viewset=ProductModelViewSet)
