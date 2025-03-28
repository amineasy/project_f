from django.db import models
from django.conf import settings


class AudioTableModel(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,editable=False ,null=True,related_name='created')
    created_on = models.DateTimeField(auto_now_add=True,editable=False)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,editable=False, null=True,related_name='modified')
    modified_on = models.DateTimeField(auto_now=True,editable=False)

    class Meta:
        abstract = True
