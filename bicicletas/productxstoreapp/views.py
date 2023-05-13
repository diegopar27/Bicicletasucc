from rest_framework.viewsets import ModelViewSet

from .models import ProdcutxStore
from .serializers import ProductxStoreSerializer


class ProductxstoreModelViewSet(ModelViewSet):
    serializer_class = ProductxStoreSerializer
    queryset = ProdcutxStore.objects.all()
    http_method_names = ['get', 'put', 'post', 'delete']

