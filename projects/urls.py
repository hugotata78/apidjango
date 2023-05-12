from django.urls import path
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'pojects')

urlpatterns = router.urls