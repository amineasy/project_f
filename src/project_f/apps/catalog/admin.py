from django.contrib import admin
from django.db.models import Count
from treebeard.forms import movenodeform_factory

from .models import *
from treebeard.admin import TreeAdmin


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)
    prepopulated_fields = {"slug": ("title",)}


class ProductClassAttributeInline(admin.TabularInline):
    model = ProductClassAttribute
    extra = 2


class ProductAttributeFilter(admin.SimpleListFilter):
    title = 'Attribute Count'
    parameter_name = 'attribute_count'

    def lookups(self, request, model_admin):
        return [
            ('more_5', 'More than 5'),
            ('lower_5', 'Lower Than 5'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'more_5':
            return queryset.annotate(attribute_count=Count('attributes_related')).filter(attribute_count__gte=5)
        if self.value() == 'lower_5':
            return queryset.annotate(attribute_count=Count('attributes_related')).filter(attribute_count__lte=5)


class ProductClassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'required_shipping', 'track_stock', 'attribute_count', 'has_attribute')
    list_filter = ('track_stock', 'required_shipping', ProductAttributeFilter)
    inlines = [ProductClassAttributeInline]
    actions = ['enable_track_stock']

    def attribute_count(self, obj):
        return obj.attributes_related.count()

    def enable_track_stock(self, request, queryset):
        queryset.update(track_stock=True)


class ProductRecommendationInline(admin.TabularInline):
    model = ProductRecommendation
    extra = 2
    fk_name = 'primary'


class ProductClassAttributeAdmin(admin.ModelAdmin):
    model = ProductClassAttribute
    list_display = ('title','type',)


class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 2


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2


class ProductItemVariantsInline(admin.TabularInline):
    model = ProductItemVariant
    extra = 2


class ProductItemAdmin(admin.ModelAdmin):
    model = ProductItem
    extra = 2
    inlines = [ProductItemVariantsInline, ProductAttributeValueInline, ProductRecommendationInline, ProductImageInline]
    prepopulated_fields = {'slug': ('title',)}


class ProductAttributeValueAdmin(admin.ModelAdmin):
    model = ProductAttributeValue
    search_fields = ['attribute__name']


class ProductItemVariantInline(admin.TabularInline):
    model = ProductItemVariant
    extra = 2


admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductClass, ProductClassAdmin)
admin.site.register(OptionGroup)
admin.site.register(OptionGroupValue)
admin.site.register(Option)
admin.site.register(ProductClassAttribute,ProductClassAttributeAdmin)
admin.site.register(ProductAttributeValue, ProductAttributeValueAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(ProductItemVariant)
