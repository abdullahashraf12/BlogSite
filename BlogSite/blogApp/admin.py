from django.contrib import admin
from .models import Category, Tag, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('categories', 'tags', 'author', 'created_at')
    search_fields = ('title', 'content','categories__name','tags__name')
    # prepopulated_fields = {'slug': ('title',)}  # If you have a slug field in Post model

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','author', 'post', 'created_at')
    list_filter = ('id','author', 'post', 'created_at')
    search_fields = ('content',)
