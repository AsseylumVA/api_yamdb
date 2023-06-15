from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODER = 'moder'
    USER = 'user'
    ROLE_CHOICES = [
        (ADMIN, 'admin'),
        (MODER, 'moderator'),
        (USER, 'user'),
    ]

    email = models.EmailField(
        'Электронная почта',
        unique=True,
    )

    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Роль',
        max_length=5,
        choices=ROLE_CHOICES,
        default=USER
    )
