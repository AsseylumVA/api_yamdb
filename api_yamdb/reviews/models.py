from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Reviews(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews', verbose_name='Автор')
    text = models.TextField()
    title = models.ForeignKey(
        Titles, on_delete=models.CASCADE,
        related_name='reviews', verbose_name='Название')
    #score = models.IntegerField()
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.text


class Comments(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments', verbose_name='Автор')
    text = models.TextField()
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
    review = models.ForeignKey(
        Reviews, on_delete=models.CASCADE,
        related_name='comments', verbose_name='Коммент на отзыв')

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text

      
class Categories(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Наименование категории'
    )
    slug = models.SlugField(
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Genres(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название жанра'
    )
    slug = models.SlugField(
        unique=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self) -> str:
        return self.name


class Titles(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Название произведения'
    )
    year = models.PositiveSmallIntegerField(
        max_length=4,
        verbose_name='Год создания произведения'
    )
    category = models.ForeignKey(
        Categories,
        null=True,
        related_name='titles',
        verbose_name='Категория произведения',
        on_delete=models.SET_NULL,

    )
    genre = models.ManyToManyField(
        Genres,
        through='TitleGenre',
        verbose_name='Описание жанра'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание произведения'
    )

    class Meta:
        ordering = ('-year',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genres,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('genre',)
        verbose_name = 'Произведение и жанр'
        verbose_name_plural = 'Произведения и жанры'

    def str(self):
        return f'Название: {self.title}, жанр: {self.genre}'
