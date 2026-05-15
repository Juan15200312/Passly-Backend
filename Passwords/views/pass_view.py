from rest_framework import viewsets, permissions
from Passwords.models import Pass
from Passwords.serializers.pass_serializer import PassSerializer

class PassViewSet(viewsets.ModelViewSet):
    serializer_class = PassSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Pass.objects.filter(user=self.request.user)
