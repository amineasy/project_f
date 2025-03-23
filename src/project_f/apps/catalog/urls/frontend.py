from rest_framework import routers

from project_f.apps.catalog.views.frontend import CategoryViewSet
from django.urls import path, include

router = routers.SimpleRouter()
router.register('categories',CategoryViewSet)
urlpatterns = [
    path('', include(router.urls)),
]