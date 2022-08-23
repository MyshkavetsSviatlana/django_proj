from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, BasePermission, \
    SAFE_METHODS
from rest_framework.response import Response
from rest_framework import viewsets, renderers

from User.models import User
from api.classroom.serializers import ClassroomSerializer
from schedule.models import Classroom


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ClassroomViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """

        if User.role == 'SuperAdmin':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [ReadOnly]
        return [permission() for permission in permission_classes]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


