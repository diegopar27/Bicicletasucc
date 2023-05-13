from rest_framework.serializers import ModelSerializer
from .models import Store


class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = ['id',
                  'created_at',
                  'name',
                  'address',
                  'contact_number',
                  'phone',
                  'email',
                  'website',
                  ]