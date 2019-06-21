from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import View, CreateView, UpdateView, DeleteView
from .models import *
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin
from .forms import TagForm, PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    tags = Tag.objects.all()
    return render(request, 'home.html', {'tags':tags})


def posts_list(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()

    return render(request, 'posts_list.html', context={'posts': posts, 'tags': tags})


def tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', context={'tags': tags})


def create_comment(request, slug):
    user = request.user
    content = request.POST.get("content")
    post = get_object_or_404(Post, slug__iexact=slug)
    Comment.objects.create(user=user, post=post, content=content)
    return redirect(reverse('posts_list'))


class PostDetail(View):
    model = Post
    template = 'post_detail.html'

    def get(self, request, slug):
        comments = Comment.objects.all().order_by('-timestamp')
        post = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): post, 'comments': comments})

    # def post(self, request, slug):
    #     post = get_object_or_404(self.model, slug__iexact=slug)
    #     comments = Comment.objects.filter(post=post).order_by('-timestamp')
    #
    #     if request.method == 'POST':
    #         comment_form = CommentForm(request.POST or None)
    #         if comment_form.is_valid():
    #             content = request.POST.get('content')
    #             comment = Comment.objects.create(post=post, user=request.user, comment=content)
    #             comment.save()
    #             return HttpResponseRedirect(post.get_absolute_url())
    #     else:
    #         comment_form = CommentForm()
    #
    #     return render(request, self.template,
    #                   context={'comments': comments, 'comment_form': comment_form})
    #


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    form = PostForm
    template_name = 'post_create.html'
    fields = ['title', 'slug', 'content', 'tags', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def get(self, request):
    #     form = PostForm
    #     return render(request, 'post_create.html', context={'form': form})
    #
    # def post(self, request):
    #     bound_form = PostForm(request.POST)
    #     if bound_form.is_valid():
    #         new_obj = bound_form.save()
    #         messages.success(request, f'{new_obj} has been created!')
    #         return redirect(new_obj)
    #     return render(request, 'post_create.html', context={'form': bound_form})


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


# class PostDelete(ObjectDeleteMixin, View):
#     model = Post
#     redirect_url = 'posts_list.html'
#     template = 'post_delete.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'tag_update.html'


# class TagDelete(ObjectDeleteMixin, View):
#     model = Tag
#     redirect_url = 'tags.html'
#     template = 'tag_delete.html'


class TagDeleteView(View):
    def get(self, request, tag_id):
        Tag.objects.filter(id=tag_id).delete()
        messages.success(request, 'Selected tag has been deleted!')
        return HttpResponseRedirect(reverse('tags'))
