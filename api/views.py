from rest_framework import generics, mixins
from .serializer import PostSerializer, CommentSerializer, ReplyCommentSerializer
from blog.models import Post, Comment, ReplyComment


class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()


class CommentAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()


class ReplyCommentAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = ReplyCommentSerializer

    def get_queryset(self):
        return ReplyComment.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReplyCommentRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ReplyCommentSerializer

    def get_queryset(self):
        return ReplyComment.objects.all()
