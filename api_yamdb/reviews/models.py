from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class Genres(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self) -> str:
        return self.title


class Titles(models.Model):
    name = models.CharField(          # название произведения
        max_length=50,
        verbose_name='Название произведения'
    )
    year = models.IntegerField(           # год
        verbose_name='Год создания произведения'
    )
    category = models.ForeignKey(       # категория
        Categories,
        related_name='titles',
        verbose_name='Категория произведения',
    )
    genre = models.ForeignKey(      # жанр
        Genres,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Жанр произведения'
    )
    description = models.TextField(            # описаие
        verbose_name='Описание произведения'
    )

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
