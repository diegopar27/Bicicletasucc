from rest_framework.viewsets import ModelViewSet

from .models import Store
from .serializers import StoreSerializer


class StoreModelViewSet(ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']