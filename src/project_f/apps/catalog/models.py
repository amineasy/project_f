from django.db import models
from treebeard.mp_tree import MP_Node

from project_f.apps.catalog.managers import CategoryQuerySet


class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(default=True)

    objects = CategoryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
