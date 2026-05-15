from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate(self, data):
        refresh_token = data.get('refresh_token')

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return {
                'success': True,
                'message': 'Se cerro la secion correctamente.',
            }
        except:
            raise serializers.ValidationError('Token invalido')


