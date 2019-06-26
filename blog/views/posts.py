from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, UpdateView, ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from ..forms import PostForm
from ..models import *


class PostListView(ListView):
    model = Post
    template_name = 'posts_list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetail(View):
    model = Post
    template = 'post_detail.html'

    def get(self, request, slug):
        tags = Tag.objects.all()
        comments = Comment.objects.all().order_by('-timestamp')
        post = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template,
                      context={self.model.__name__.lower(): post, 'comments': comments, 'tags': tags})


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form = PostForm
    template_name = 'post_create.html'
    fields = ['title', 'slug', 'content', 'tags', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form = PostForm
    template_name = 'post_update_form.html'
    fields = ['title', 'slug', 'content', 'tags', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(View):
    def get(self, request, post_id):
        Post.objects.filter(id=post_id).delete()
        messages.success(request, 'Selected post has been deleted!')
        return HttpResponseRedirect(reverse('posts_list'))
