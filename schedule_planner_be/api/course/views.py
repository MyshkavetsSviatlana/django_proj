from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, viewsets, renderers
from api.course.serializers import CourseSerializer
from course.models import Course


class CourseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        course = self.get_object()
        return Response(course.highlighted)
