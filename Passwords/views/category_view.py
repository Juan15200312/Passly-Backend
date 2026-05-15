from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from Passwords.models import Category
from Passwords.serializers.category_serializer import CategorySerializer


class CategoryView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

    def get(self,request,*args,**kwargs):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)