# Generated by Django 2.2.19 on 2023-06-12 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название категории')),
                ('slug', models.SlugField(unique=True, verbose_name='Уникальный элемент категории')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название задачи', max_length=50, verbose_name='Название задачи')),
                ('description', models.TextField(verbose_name='Описание задачи')),
                ('deadline', models.DateTimeField(verbose_name='Срок выполнения')),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', models.ForeignKey(blank=True, help_text='Категория для задачи', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', to='tasks.Category', verbose_name='Категория')),
            ],
        ),
    ]