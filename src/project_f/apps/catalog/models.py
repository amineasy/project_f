from django.db import models
from treebeard.mp_tree import MP_Node


class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(default=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
