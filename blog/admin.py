from django.contrib import admin

from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag, TagAdmin)

