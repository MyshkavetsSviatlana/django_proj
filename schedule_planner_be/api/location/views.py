from rest_framework import viewsets, permissions
from api.location.serializers import LocationSerializer
from schedule.models import Location
from User.models import User


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
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
