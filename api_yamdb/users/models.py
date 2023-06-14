from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODER = 'moderator'
    USER = 'user'
    ROLE_CHOICES = [
        (ADMIN, 'admin'),
        (MODER, 'moderator'),
        (USER, 'user'),
    ]

    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        choices=ROLE_CHOICES,
        default=USER
    )
