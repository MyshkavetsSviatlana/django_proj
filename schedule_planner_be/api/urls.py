from django.urls import path, include


urlpatterns = [
    path('users/', include('api.user.urls')),
    path('teachers/', include('api.teacher.urls')),
    path('courses/', include('api.course.urls')),
]