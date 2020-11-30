# Generated by Django 3.1.3 on 2020-11-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogsection_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='sections',
            field=models.ManyToManyField(related_name='relate_posts', to='blog.BlogSection', verbose_name='Разделы, в которых опубликован пост'),
        ),
    ]