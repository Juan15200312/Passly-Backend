from django.db import models
from decouple import config
from cryptography.fernet import Fernet


class Pass(models.Model):
    title = models.CharField(max_length=100, default='Sin Título')
    username = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=512)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='passes')

    user = models.ForeignKey('Users.CustomUser', on_delete=models.CASCADE, related_name='passwords')

    def __str__(self):
        return f'{self.title} - {self.user.email}'

    def set_password(self, raw_password):
        key = config('ENCRYPTION_KEY')
        f = Fernet(key.encode())
        self.password = f.encrypt(raw_password.encode()).decode()

    def get_password(self):
        try:
            key = config('ENCRYPTION_KEY')
            f = Fernet(key.encode())
            return f.decrypt(self.password.encode()).decode()
        except Exception:
            return ""

    class Meta:
        verbose_name = 'Contraseña'
        verbose_name_plural = '1. Contraseñas'