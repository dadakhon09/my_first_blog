from django.contrib import admin
from .models import Post, Tag, Comment, ReplyComment



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'slug')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Tag, TagAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'content')
    search_fields = ['user', 'post', 'content']


admin.site.register(Comment, CommentAdmin)


class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment_reply', 'content')
    search_fields = ['user', 'comment_reply', 'content']

admin.site.register(ReplyComment, ReplyCommentAdmin)


