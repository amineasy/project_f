import hashlib

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from project_f.apps.media.exception import DuplicateImageException


class Image(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(height_field="height", width_field="width", upload_to='images/')
    width = models.IntegerField(editable=False, null=True, blank=True)
    height = models.IntegerField(editable=False, null=True, blank=True)
    file_hash = models.CharField(max_length=40, db_index=True, blank=True, null=True)
    file_size = models.PositiveIntegerField(null=True, blank=True)

    focal_point_x = models.PositiveIntegerField(null=True, blank=True)
    focal_point_y = models.PositiveIntegerField(null=True, blank=True)
    focal_point_width = models.PositiveIntegerField(null=True, blank=True)
    focal_point_height = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.file_size = self.image.size

        hasher = hashlib.sha1()
        for chunk in self.image.file.chunks():
            hasher.update(chunk)
        self.file_hash = hasher.hexdigest()

        super().save(*args, **kwargs)


@receiver(pre_save, sender=Image)
def chunk_duplicate_hash(sender, instance, **kwargs):
    existed = Image.objects.filter(file_hash=instance.file_hash).exists()
    if existed:
        raise DuplicateImageException('duplicate image')
