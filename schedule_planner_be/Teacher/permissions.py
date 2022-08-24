class TeacherPermissionsMixin:
    def has_permissions(self):
        return self.request.user.role == 'Super Admin'
