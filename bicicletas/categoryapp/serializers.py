from rest_framework.serializers import ModelSerializer
from categoryapp.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id',
                  'created_at',
                  'name',
                  ]