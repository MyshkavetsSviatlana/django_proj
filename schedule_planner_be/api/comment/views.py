from rest_framework import viewsets
from api.comment.serializers import CommentSerializer
from schedule.models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


