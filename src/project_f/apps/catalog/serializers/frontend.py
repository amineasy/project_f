from rest_framework import serializers
from project_f.apps.catalog.models import Category, OptionGroup, OptionGroupValue


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OptionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionGroup
        fields = '__all__'


class OptionGroupValueSerializer(serializers.ModelSerializer):


    OptionGroup = OptionGroupSerializer(many=True, read_only=True)

    class Meta:
        model = OptionGroupValue

        fields = ['title', 'OptionGroup']
