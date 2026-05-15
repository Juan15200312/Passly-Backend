from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from Users.serializers.user_serializer import UserSerializerPart


class ProfileView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializerPart(request.user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        if 'first_name' in data:
            user.first_name = data['first_name']
        if 'last_name' in data:
            user.last_name = data['last_name']

        if 'image' in request.FILES:
            if user.info:
                user.info.image = request.FILES['image']
                user.info.save()

        if 'password' in data and data['password']:
            user.set_password(data['password'])

        user.save()

        serializer = UserSerializerPart(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
