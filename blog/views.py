from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, CreateView, UpdateView
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin
from .forms import TagForm, PostForm
from django.contrib import messages
from users.models import Profile


def home(request):
    return render(request, 'home.html', {})


def posts_list(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, 'posts_list.html', context={'posts': posts, 'tags': tags})


def tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'post_detail.html'


class PostCreate(Profile,CreateView):
    model = Post
    form = PostForm
    template_name = 'post_create.html'
    fields = ['title', 'slug', 'content', 'tags', 'image']

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


class PostUpdate(UpdateView):
    model = Post
    form = PostForm
    template_name = 'post_update_form.html'
    fields = ['title', 'slug', 'content', 'tags', 'image']


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


class PostDeleteView(View):
    def get(self, request, post_id):
        Post.objects.filter(id=post_id).delete()
        messages.success(request, 'Selected post has been deleted!')
        return HttpResponseRedirect(reverse('posts_list'))


