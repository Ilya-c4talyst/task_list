from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Уникальный элемент категории'
    )

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название задачи',
        help_text='Введите название задачи'
    )
    author = models.CharField(
        max_length=50
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='tasks',
        blank=True,
        null=True,
        verbose_name='Категория',
        help_text='Категория для задачи'
    )
    description = models.TextField(
        verbose_name='Описание задачи'
    )
    deadline = models.DateTimeField(
        verbose_name='Срок выполнения'
    )
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
