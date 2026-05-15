from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from Users.models import CustomUser
from Users.serializers.user_serializer import UserSerializerPart


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(min_length=8)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = CustomUser.objects.filter(email=email).first()

        if not user:
            raise serializers.ValidationError('Credenciales inválidas. Verifica tu email y contraseña.')

        if not user.check_password(password):
            raise serializers.ValidationError('Credenciales inválidas. Verifica tu email y contraseña.')


        refresh_token = RefreshToken.for_user(user)
        token = refresh_token.access_token

        user_serializer = UserSerializerPart(user, context=self.context)

        return {
            'success': True,
            'refresh_token': str(refresh_token),
            'token': str(token),
            'user': user_serializer.data
        }

