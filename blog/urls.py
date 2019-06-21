from django.urls import path
from blog.views import *

urlpatterns = [
    path('posts/', posts_list, name="posts_list"),
    path('post/<str:slug>/', PostDetail.as_view(), name="post_detail"),
    path('post/<str:slug>/comment', create_comment, name="comment_create_url"),
    path('posts/create/', PostCreate.as_view(), name="post_create"),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name="post_update"),
    # path('post/<str:slug>/delete/', PostDelete.as_view(), name="post_delete"),
    path('post/new-delete/<int:post_id>/', PostDeleteView.as_view(), name="post_new_delete"),
    path('tags/', tags, name="tags"),
    path('tag/<str:slug>/', TagDetail.as_view(), name="tag_detail"),
    path('tags/create/', TagCreate.as_view(), name="tag_create"),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name="tag_update"),
    # path('tag/<str:slug>/delete/', TagDelete.as_view(), name="tag_delete"),
    path('tag/new-delete/<int:tag_id>/', TagDeleteView.as_view(), name="tag_new_delete"),
]
