from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time']
    search_fields = ['name']
    list_filter = ['name']
    show_full_result_count = True
    save_as = True
    save_on_continue = True

@admin.register(ArticleInfo)
class ArticleInfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'create_time', 'author', 'desc']
    search_fields = ['title']
    list_filter = ['title']
    show_full_result_count = True
    save_as = True
    save_on_continue = True
