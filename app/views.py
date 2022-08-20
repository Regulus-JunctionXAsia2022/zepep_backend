from rest_framework.generics import ListCreateAPIView, UpdateAPIView, GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from rest_framework.exceptions import ParseError, PermissionDenied
from rest_framework.response import Response
from app.models import Zepep

from app.serializers import ZepepModelSerializer


class ZepepListCreateAPIView(ListCreateAPIView):
    serializer_class = ZepepModelSerializer

    def get_queryset(self):
        try:
            zepep_id = self.request.query_params['zepep_id']
            user_id = self.request.query_params['user_id']
            zepep = Zepep.objects.get(id=zepep_id)
        except KeyError:
            raise ParseError('Zepep id and user id is not given')
        except Zepep.DoesNotExist:
            raise ParseError('Zepep with given id does not exists')

        if zepep.user != user_id:
            raise PermissionDenied(
                'This user is not allowed to retrieve this zepep')
        return Zepep.objects.filter(id=zepep.id)


class ZepepUpdateAPIView(GenericAPIView
                         ):
    queryset = Zepep.objects.all()
    serializer_class = ZepepModelSerializer
    lookup_url_kwarg = 'zepep_id'

    def post(self, request, zepep_id=None):

        if not zepep_id:
            raise ParseError('Zepep id is not given')
        try:
            user_id = request.data['user_id']
        except KeyError:
            raise ParseError('User id is not given')
        except Zepep.DoesNotExist:
            raise ParseError('Zepep with given id does not exists')
        zepep = Zepep.objects.get(id=zepep_id)
        if zepep.user != user_id:
            raise PermissionDenied(
                'This user is not allowed to retrieve this zepep')

        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
