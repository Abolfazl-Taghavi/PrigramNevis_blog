from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'datetime_updated', 'status')
    ordering = ('datetime_updated', 'status', '-title', 'author')

