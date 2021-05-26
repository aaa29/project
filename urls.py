from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('forum.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
]
