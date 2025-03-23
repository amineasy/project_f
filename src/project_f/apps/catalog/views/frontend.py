from rest_framework import viewsets

from project_f.apps.catalog.models import Category
from project_f.apps.catalog.serializers.frontend import CategorySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.public()
    serializer_class = CategorySerializer
