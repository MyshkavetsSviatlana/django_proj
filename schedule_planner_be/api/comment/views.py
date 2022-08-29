from rest_framework import viewsets, permissions
from api.comment.serializers import CommentSerializer
from schedule.models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user_role = self.request.user.role
        if user_role == 'Super Admin':
            return True
        raise PermissionError('User has not permission')

    def update(self, request, *args, **kwargs):
        user_role = self.request.user.role
        if user_role == 'Super Admin':
            return True
        raise PermissionError('User has not permission')

    def destroy(self, request, *args, **kwargs):
        user_role = self.request.user.role
        if user_role == 'Super Admin':
            return True
        raise PermissionError('User has not permission')
