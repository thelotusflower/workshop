from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from blog.querysets import BlogSectionQS


class BlogSection(models.Model):
    name = models.CharField(max_length=100, verbose_name='Раздел блога')
    slug = models.SlugField(
        verbose_name='Название раздела в ссылке',
        unique=True,
        allow_unicode=True
    )
    # добавить views_per_day по разделу позже и сделать миграцию данных, которая заполнит значения
    # views_per_day = models.PositiveIntegerField(
    #     verbose_name='Количество просмотров постов раздела в день'
    # )

    objects = BlogSectionQS.as_manager()

    def __str__(self):
        return f'{self.name}'


class BlogPost(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название поста')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Создатель поста')
    text = models.TextField(verbose_name='Текст поста')
    slug = models.SlugField(verbose_name='Название поста в ссылке', allow_unicode=True, unique=True) 
    short_description = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Краткое содержание поста'
    )
    sections = models.ManyToManyField(
        BlogSection,
        verbose_name='Разделы, в которых опубликован пост',
        related_name='relate_posts'
    )
    view_count = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров поста')


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(force_insert, force_update, using, update_fields)


class Tag(models.Model):
    name = models.CharField(max_length=20)
