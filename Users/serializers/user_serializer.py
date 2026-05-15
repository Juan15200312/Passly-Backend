from rest_framework import serializers

from Users.models import CustomUser
from Users.serializers.info_serializer import InfoSerializer


class UserReadSerializer(serializers.ModelSerializer):  # INFORMACIÓN COMPLETA
    info = InfoSerializer()

    class Meta:
        model = CustomUser
        fields = ('slug', 'email', 'first_name', 'last_name', 'info')
        read_only_fields = ('slug', 'email', 'first_name', 'last_name', 'info')


class UserSerializerPart(serializers.ModelSerializer): # INFORMACIÓN PARCIAL
    image = serializers.ImageField(source='info.image', read_only=True)

    class Meta:
        model = CustomUser
        fields = ('slug', 'email', 'first_name', 'last_name', 'image')