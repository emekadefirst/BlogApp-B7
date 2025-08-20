from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    search_fields = ['name']
    ordering = ['-created_at', '-updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    list_filter = ['category', 'created_at', 'updated_at']
    ordering = ['-created_at', '-updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']

admin.site.register(Post, PostAdmin)