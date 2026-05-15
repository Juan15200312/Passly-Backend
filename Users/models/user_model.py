import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self,first_name=None, last_name=None,email=None, password=None, **extra_fields):
        if not first_name or not last_name:
            raise ValueError('Los nombres y apellidos deben de ser obligatorios.')

        if not email:
            raise ValueError('El correo electrónico es obligatorio.')

        if not password:
            raise ValueError('La contraseña es obligatorio.')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name=None, last_name=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(first_name, last_name, email, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=100, verbose_name='Nombres')
    last_name = models.CharField(max_length=100, verbose_name='Apellidos')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    is_superuser = models.BooleanField(default=False, verbose_name='¿Es superusuario?')
    is_staff = models.BooleanField(default=False, verbose_name='¿Es del personal?')
    is_active = models.BooleanField(default=True, verbose_name='¿Esta activo?')

    info = models.OneToOneField('Info', on_delete=models.CASCADE, null=True, blank=True, related_name='user', verbose_name='Información')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        if not self.slug:
            prov = uuid.uuid4().hex
            while CustomUser.objects.filter(slug=prov).exists():
                prov = uuid.uuid4().hex
            self.slug = prov

        super().save(*args, **kwargs)

        if is_new and self.info is None:
            from .info_model import Info
            info = Info.objects.create()
            self.info = info
            super().save(update_fields=['info'])


    class Meta:
        db_table = 'users'
        ordering = ('email',)
        verbose_name = 'Usuario'
        verbose_name_plural = '1. Usuarios'
