from rest_framework import routers
from project_f.apps.catalog.views.frontend import CategoryViewSet, OptionGroupViewSet, OptionGroupValueViewSet
from django.urls import path, include

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('option-groups', OptionGroupViewSet)
router.register('OptionGroupValue', OptionGroupValueViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
