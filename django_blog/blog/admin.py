from django.contrib import admin

from blog.models import BlogSection, BlogPost

# Как джанго ищет админские файлы самостоятельно, когда подключено приложение админки

# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#discovery-of-admin-files

admin.site.register(BlogSection)
admin.site.register(BlogPost)
