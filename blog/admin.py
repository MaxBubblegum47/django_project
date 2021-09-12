from django.contrib import admin
from .models import Post, Comment, Category, Report

# Register your models here.
# admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Report)


@admin.register(Post)
class ThreadAdmin(admin.ModelAdmin):
    search_fields = ['category']
    list_display = ('title', 'category')
