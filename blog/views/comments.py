from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

from ..models import Comment, ReplyComment, Post


# comments
def create_comment(request, slug):
    user = request.user
    content = request.POST.get("content")
    post = get_object_or_404(Post, slug__iexact=slug)
    Comment.objects.create(user=user, post=post, content=content)
    return redirect(reverse('post_detail', kwargs={'slug': slug}))


def create_reply(request, slug, pk):
    user = request.user
    content = request.POST.get("content")
    comment = get_object_or_404(Comment, pk=pk)
    ReplyComment.objects.create(user=user, comment_reply=comment, content=content)
    return redirect(reverse('post_detail', kwargs={'slug': slug}))
