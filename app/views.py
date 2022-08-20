from rest_framework.generics import ListCreateAPIView
from app.models import Zepep

from app.serializers import ZepepModelSerializer


class ZepepListCreateAPIView(ListCreateAPIView):
    queryset = Zepep.objects.all()
    serializer_class = ZepepModelSerializer
