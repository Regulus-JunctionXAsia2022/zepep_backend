from dataclasses import field
from rest_framework.serializers import Serializer, ModelSerializer
from .models import Zepep


class ZepepModelSerializer(ModelSerializer):

    class Meta:
        model = Zepep
        fields = '__all__'
