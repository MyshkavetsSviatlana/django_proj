from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, viewsets, renderers
from api.classroom.serializers import ClassroomSerializer
from schedule.models import Classroom


class ClassroomViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)


