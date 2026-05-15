from rest_framework import serializers

from Passwords.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'slug', 'name', 'color', 'icon')


