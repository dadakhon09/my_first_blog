from rest_framework import serializers
from blog.models import Post, Comment, ReplyComment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'created_on', 'tags')
        read_only_fields = ['id', 'author']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'post', 'content', 'user', 'timestamp')
        read_only_fields = ['id', 'user']


class ReplyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyComment
        fields = ('id', 'comment_reply', 'content', 'user', 'timestamp')
        read_only_fields = ['id', 'user']
