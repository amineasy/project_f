from django.contrib import admin
from treebeard.forms import movenodeform_factory

from .models import *
from treebeard.admin import TreeAdmin


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Category, CategoryAdmin)
