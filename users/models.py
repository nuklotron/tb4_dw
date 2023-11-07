from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractBaseUser):
    username = None
    phone = models.CharField(unique=True, max_length=15, verbose_name='Phone')
    email = models.EmailField(verbose_name='email', **NULLABLE)
    first_name = models.CharField(max_length=50, verbose_name='First name', **NULLABLE)
    last_name = models.CharField(max_length=50, verbose_name='Last name', **NULLABLE)
    invite_code = models.CharField(max_length=6, verbose_name='Invite_code', **NULLABLE)
    passcode = models.SmallIntegerField(verbose_name='Passcode', **NULLABLE)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
