from rest_framework import serializers
from Passwords.models import Pass
from Passwords.serializers.category_serializer import CategorySerializer

class PassSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source='category', read_only=True)
    password_decrypted = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Pass
        fields = ['id', 'title', 'username', 'url', 'notes', 'icon', 'category', 'category_detail', 'password', 'password_decrypted']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_password_decrypted(self, obj):
        return obj.get_password()

    def create(self, validated_data):
        raw_password = validated_data.pop('password')
        user = self.context['request'].user
        instance = Pass(**validated_data, user=user)
        instance.set_password(raw_password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        raw_password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if raw_password:
            instance.set_password(raw_password)
        instance.save()
        return instance
