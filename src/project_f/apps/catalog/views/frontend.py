from rest_framework import viewsets

from project_f.apps.catalog.models import Category, OptionGroup, OptionGroupValue
from project_f.apps.catalog.serializers.frontend import CategorySerializer, OptionGroupSerializer, \
    OptionGroupValueSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.public()
    serializer_class = CategorySerializer


class OptionGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OptionGroup.objects.all()
    serializer_class = OptionGroupSerializer



class OptionGroupValueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OptionGroupValue.objects.all()
    serializer_class = OptionGroupValueSerializer