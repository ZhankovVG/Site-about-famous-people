from django.db import models
from django.urls import reverse


class Men(models.Model):
    title = models.CharField(max_length=175, verbose_name='Название')
    content = models.TextField(blank=True,verbose_name='Текст')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Url')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d',verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Создание даты')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Добавление даты')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Известные актеры'
        verbose_name_plural = 'Известные актеры'
        ordering =['title']

    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_slug' : self.slug } )

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Имя')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Url')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    def get_absolute_url(self):
        return reverse('category', kwargs = {'cat_id' : self.pk } )
        