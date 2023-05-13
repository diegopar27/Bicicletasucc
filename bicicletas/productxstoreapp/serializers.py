from rest_framework.serializers import ModelSerializer
from .models import ProdcutxStore


class ProductxStoreSerializer(ModelSerializer):
    class Meta:
        model = ProdcutxStore
        fields = ['id',
                  'created_at',
                  'store',
                  'product',
                  ]
