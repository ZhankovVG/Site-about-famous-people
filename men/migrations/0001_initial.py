# Generated by Django 4.1.3 on 2023-02-12 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Men',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=175, verbose_name='Название')),
                ('content', models.TextField(blank=True, verbose_name='Текст')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Создание даты')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Добавление даты')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='men.category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Известные актеры',
                'verbose_name_plural': 'Известные актеры',
                'ordering': ['title'],
            },
        ),
    ]
