from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import permissions, viewsets, renderers, generics
from api.course.serializers import CourseSerializer
from course.models import Course
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import CoursePermissionsMixin
from .service import CourseFilter


class CourseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     if self.action == 'list':
    #         permission_classes = [IsAuthenticated]
    #     else:
    #         permission_classes = [IsAuthenticated & CoursePermissionsMixin]
    #     return [permission() for permission in permission_classes]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        course = self.get_object()
        return Response(course.highlighted)


class CourseMorningListView(generics.ListAPIView):
    """Вывод утреннего расписания"""
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CourseFilter

    def get_queryset(self):
        courses = Course.objects.all().filter(course_type__contains='Morning schedule')
        return courses


class CourseEveningListView(generics.ListAPIView):
    """Вывод утреннего расписания"""
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CourseFilter

    def get_queryset(self):
        courses = Course.objects.all().filter(course_type__contains='Evening schedule')
        return courses
