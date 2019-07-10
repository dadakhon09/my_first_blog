from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
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


class CommentCreateAPIView(APIView):
    def post(self, request, post_id):
        text = request.POST.get('text')
        c = Comment(post_id=post_id, user=request.user, content=text)
        c.save()
        cs = CommentSerializer(c)
        return Response(data={'comment': cs.data, 'reply_count': c.reply.count()})


class ReplyCreateAPIView(APIView):
    def post(self, request, com_id):
        text = request.POST.get('text')
        c = ReplyComment(comment_reply_id=com_id, user=request.user, content=text)
        c.save()
        cs = ReplyCommentSerializer(c)
        return Response(data={'reply': cs.data})

class PostCreateAPIView(APIView):
    def post(self, request, author_id):
        text = request.POST.get('text')
        title = request.POST.get('title')
        p = Post(author_id=author_id, title=title, content=text)
        p.save()
        cs = PostSerializer(p)
        return Response(data={'post': cs.data})





    # title = models.CharField(max_length=200, unique=True, db_index=True)
    # slug = models.SlugField(max_length=200, blank=True)
    # content = models.TextField(null=True, db_index=True)
    # tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    # created_on = models.DateField(auto_now_add=True)
    # author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='author_posts')
    # image = models.ImageField(default='default_post.jpg', blank=True, null=True, upload_to='post_pics')
