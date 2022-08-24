from django.urls import path, include


urlpatterns = [
    path('', include('api.user.urls')),
    path('teachers/', include('api.teacher.urls')),
    path('courses/', include('api.course.urls')),
    path('classrooms/', include('api.classroom.urls')),
    path('subwaystations/', include('api.subwaystation.urls')),
]