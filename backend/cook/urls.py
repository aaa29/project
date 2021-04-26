from django.urls import include, path
from rest_framework import routers
from .views import IngViewSet

router = routers.DefaultRouter()
router.register('ings', IngViewSet)

urlpatterns = [
    path('', include(router.urls))
]