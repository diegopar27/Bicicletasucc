from rest_framework.routers import DefaultRouter
from .views import ProductxstoreModelViewSet


router_Productxstore = DefaultRouter()

router_Productxstore.register(prefix='Productxstore', basename='Productxstore',
                              viewset=ProductxstoreModelViewSet)
