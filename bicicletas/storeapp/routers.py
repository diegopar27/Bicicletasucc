from rest_framework.routers import DefaultRouter
from .views import StoreModelViewSet


router_store = DefaultRouter()

router_store.register(prefix='store', basename='store', viewset=StoreModelViewSet)
