from django.db import models
from PIL import Image


class Info(models.Model):
    phone = models.CharField(max_length=15, null=True, blank=True, verbose_name='Teléfono')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Fecha de nacimiento')
    image = models.ImageField(upload_to='images/users_images/',null=True, blank=True, verbose_name='Imagen')

    def __str__(self):
        return self.user.__str__()

    class Meta:
        db_table = 'users_info'
        verbose_name = 'Información'
        verbose_name_plural = '2. Informaciones'