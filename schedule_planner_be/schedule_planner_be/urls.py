from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .swagger import urlpatterns as doc_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='User/home.html'), name='home'),
    path('courses/', include('course.urls')),
    path('teachers/', include('Teacher.urls')),
    path('user/', include('User.urls')),
    path('user/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('api.urls')),
]


urlpatterns += [
    path("schedule/", include('schedule.urls')),
]

urlpatterns += doc_urls

