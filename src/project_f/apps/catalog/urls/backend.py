from rest_framework import routers

from project_f.apps.catalog.views.backend import CategoryViewSet


app_name = 'catalog'

router = routers.SimpleRouter()
router.register('categories',CategoryViewSet,basename='category')
urlpatterns = [] + router.urls