from rest_framework.routers import DefaultRouter
from .views import CategoryModelViewSet


router_Category = DefaultRouter()

router_Category.register(prefix='Category', basename='Category', viewset=CategoryModelViewSet)
