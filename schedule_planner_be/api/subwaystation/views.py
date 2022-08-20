from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, renderers
from api.subwaystation.serializers import SubwayStationSerializer
from schedule.models import SubwayStation


class SubwayStationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = SubwayStation.objects.all()
    serializer_class = SubwayStationSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)



