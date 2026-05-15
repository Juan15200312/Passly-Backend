from rest_framework import serializers

from Users.models import Info


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('phone', 'birth_date', 'image')