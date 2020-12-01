from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import os

from .managers import DishManager


def custom_save_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('img/', filename)


class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'


class Dish(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    ingredients = models.ManyToManyField(
        Ingredient, verbose_name='ингредиенты', through='DishIngredient')
    img = models.ImageField(upload_to=custom_save_path,
                            verbose_name='изображение', default='img/no-image.png')
    bookmarks = models.ManyToManyField(
        User, verbose_name='закладки', blank=True)
    description = models.TextField(verbose_name='рецепт')
    objects = DishManager.as_manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'блюдо'
        verbose_name_plural = 'блюда'


class DishIngredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    weight = models.IntegerField()

    def __str__(self):
        return str(self.dish) + ': ' + str(self.ingredient)

    class Meta:
        verbose_name = 'блюдо-ингредиент'
        verbose_name_plural = 'блюда-ингредиенты'


class Comment(models.Model):
    article = models.ForeignKey(Dish, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Комментарий')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.article) + ': ' + str(self.author) + ': ' + str(self.content)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок вопроса')
    content = models.TextField(verbose_name='Текст вопроса')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Ответ')
    author = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
