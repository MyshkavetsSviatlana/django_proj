from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework import viewsets, renderers

from User.models import User
from api.subwaystation.serializers import SubwayStationSerializer
from schedule.models import SubwayStation


# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS


class SubwayStationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = SubwayStation.objects.all()
    serializer_class = SubwayStationSerializer

    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     if User.role == 'Super Admin':
    #         permission_classes = [IsAdminUser]
    #     else:
    #         permission_classes = [ReadOnly]
    #     return [permission() for permission in permission_classes]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)



