from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import View, CreateView, UpdateView, ListView, DeleteView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator

from users.models import Profile
from ..forms import PostForm
from ..models import *


class PostListView(LoginRequiredMixin, ListView):
    # model = Post
    # template_name = 'posts_list.html'
    # context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


    def get(self,request):
        p = Post.objects.all()
        paginator = Paginator(p, 3)

        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'posts_list.html', {'posts':posts})



class PostDetail(LoginRequiredMixin, View):
    model = Post
    template = 'post_detail.html'

    def get(self, request, slug):
        comments = Comment.objects.all().order_by('-timestamp')
        post = get_object_or_404(self.model, slug__iexact=slug)
        is_liked = False
        is_saved = False
        if post.saves.filter(id=request.user.id).exists():
            is_saved = True
        if post.likes.filter(id=request.user.id).exists():
            is_liked = True
        return render(request, self.template,
                      context={self.model.__name__.lower(): post, 'comments': comments, 'is_liked':is_liked, 'is_saved':is_saved})



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


class PostDeleteView(LoginRequiredMixin,View):
    def get(self, request, post_id):
        Post.objects.filter(id=post_id).delete()
        messages.success(request, 'Selected post has been deleted!')
        return HttpResponseRedirect(reverse('posts_list'))

class LikePost(LoginRequiredMixin,View):
    def post(self,request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs['post_id'])
        is_liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            is_liked = False
        else:
            post.likes.add(request.user)
            is_liked = True
        return HttpResponse(status='200')

class SavePost(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs['post_id'])
        is_saved = False
        if post.saves.filter(id=request.user.id).exists():
            post.saves.remove(request.user)
            is_saved = False
        else:
            post.saves.add(request.user)
            is_saved = True
        return HttpResponse(status='200')
