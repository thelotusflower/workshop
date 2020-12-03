from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from blog.models import BlogSection, BlogPost

# Как джанго ищет админские файлы самостоятельно, когда подключено приложение админки

# https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#discovery-of-admin-files

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'slug', 'short_description', 'view_count')
    readonly_fields = ('view_count', 'post_url')

    def post_url(self, instance):
        return mark_safe(f'<a href="{reverse("blog:post", kwargs={"slug": instance.slug})}">Ссылка на пост</a>')

admin.site.register(BlogSection)
admin.site.register(BlogPost, BlogPostAdmin)
