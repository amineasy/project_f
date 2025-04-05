from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import ForeignKey
from treebeard.mp_tree import MP_Node

from project_f.apps.catalog.managers import CategoryQuerySet
from project_f.libs.db.fields import UppercaseCharField
from project_f.libs.db.models import AudioTableModel


class Category(MP_Node):
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField(null=True, blank=True)
    is_public = models.BooleanField(default=True)

    objects = CategoryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class OptionGroup(models.Model):
    title = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Option Group'
        verbose_name_plural = "Option Groups"


class OptionGroupValue(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Option Group value'
        verbose_name_plural = "Option Group values"


class ProductClass(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='categories_product_class',blank=True, null=True)
    title = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField()

    track_stock = models.BooleanField(default=True)
    required_shipping = models.BooleanField(default=True)

    @property
    def has_attribute(self):
        return self.attributes_related.exists()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product class'
        verbose_name_plural = "Product classes"


class ProductClassAttribute(models.Model):
    class AttributeTypeChoice(models.TextChoices):
        TEXT = ('text', 'Text')
        INTEGER = ('integer', 'Integer')
        FLOAT = ('float', 'Float')
        BOOLEAN = ('boolean', 'Boolean')
        DATE = ('date', 'Date')
        TIME = ('time', 'Time')
        OPTION = ('option', 'Option')
        MULTI_OPTION = ('multi_option', 'Multi Option')

    product = models.ForeignKey(ProductClass, on_delete=models.CASCADE, null=True, related_name='attributes_related')
    title = models.CharField(max_length=255, db_index=True)
    type = models.CharField(max_length=16, choices=AttributeTypeChoice.choices, default=AttributeTypeChoice.TEXT)
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Product class Attribute'
        verbose_name_plural = "Product class Attributes"


class Option(models.Model):
    class OptionTypeChoice(models.TextChoices):
        TEXT = ('text', 'Text')
        INTEGER = ('integer', 'Integer')
        FLOAT = ('float', 'Float')
        BOOLEAN = ('boolean', 'Boolean')
        DATE = ('date', 'Date')
        TIME = ('time', 'Time')
        OPTION = ('option', 'Option')
        MULTI_OPTION = ('multi_option', 'Multi Option')

    title = models.CharField(max_length=255, db_index=True)
    type = models.CharField(max_length=16, choices=OptionTypeChoice.choices, default=OptionTypeChoice.TEXT)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, null=True, blank=True)
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = "Options"


class ProductItem(AudioTableModel):
    product_class = models.ForeignKey(ProductClass, on_delete=models.PROTECT, null=True, blank=True)

    class ProductTypeChoice(models.TextChoices):
        standalone = ('standalone', 'Standalone')
        parent = ('parent', 'Parent')
        child = ('child', 'Child')

    structure = models.CharField(max_length=16, choices=ProductTypeChoice.choices, default=ProductTypeChoice.standalone)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=128, null=True, blank=True)
    slug = models.SlugField(unique=True, allow_unicode=True)
    upc = UppercaseCharField(max_length=24, null=True, blank=True, unique=True)
    is_public = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=128, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)

    attributes = models.ManyToManyField(ProductClassAttribute, through='ProductAttributeValue')
    recommended_product = models.ManyToManyField('catalog.ProductItem', through='ProductRecommendation', blank=True)
    category = models.ManyToManyField(Category, related_name='categories')
    option_groups = models.ManyToManyField(OptionGroup, related_name='option_groups',blank=True, null=True)
    options = models.ManyToManyField(OptionGroupValue, blank=True,null=True, related_name='options')

    @property
    def main_image(self):
        if self.images.exists():
            return self.images.first()
        else:
            return None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ProductItem'
        verbose_name_plural = "Product Items"


class ProductAttributeValue(models.Model):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    attribute = models.ForeignKey(ProductClassAttribute, on_delete=models.CASCADE)
    value_text = models.TextField(null=True, blank=True)
    value_integer = models.IntegerField(null=True, blank=True)
    value_float = models.FloatField(null=True, blank=True)
    value_date = models.DateField(null=True, blank=True)
    value_time = models.TimeField(null=True, blank=True)
    value_boolean = models.BooleanField(default=False)

    value_option = models.ForeignKey(OptionGroupValue, on_delete=models.PROTECT, null=True, blank=True,
                                     related_name='attributes_related')

    def __str__(self):
        match True:
            case _ if self.value_text:
                return f"{str(self.value_text)} {str(self.attribute)}"
            case _ if self.value_integer is not None:
                return f"{str(self.value_integer)} {str(self.attribute)}"
            case _ if self.value_float is not None:
                return f"{str(self.value_float)} {str(self.attribute)}"
            case _ if self.value_date:
                return f"{str(self.value_date)} {str(self.attribute)}"
            case _ if self.value_time:
                return f"{str(self.value_time)} {str(self.attribute)}"
            case _ if self.value_option:
                return f"{str(self.value_option)} {str(self.attribute)}"
            case _:
                return "No Value"

    class Meta:
        verbose_name = 'Product Attribute Value'
        verbose_name_plural = "Product Attribute Values"
        unique_together = (('product_item', 'attribute'),)


class ProductRecommendation(models.Model):
    primary = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='primary_recommendation')
    recommendation = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    rank = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = (('primary', 'recommendation'),)
        ordering = ('primary', '-rank')


class ProductImage(models.Model):
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='images')
    image = ForeignKey('media.Image', on_delete=models.PROTECT)
    display_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ('display_order',)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.images.all()
        for index, image in enumerate(self.product.images.all()):
            image.display_order = index
            image.save()


class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hex_code = models.CharField(max_length=7, unique=True)  # مثلا "#FF5733"

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ProductItemVariant(models.Model):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name="variants")
    color = models.ForeignKey(Color, on_delete=models.PROTECT, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.PROTECT, null=True, blank=True)
    price = models.IntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product_item", "color", "size"],
                name="unique_variant"
            ),
        ]

    def __str__(self):
        details = []
        if self.color:
            details.append(f"Color: {self.color}")
        if self.size:
            details.append(f"Size: {self.size}")
        return f"{self.product_item.title} - " + " | ".join(details)
