from rest_framework import routers

from project_f.apps.catalog.views.frontend import CategoryViewSet

router = routers.SimpleRouter()
router.register('categories',CategoryViewSet)
urlpatterns = [] + router.urls