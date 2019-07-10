from django.urls import path, include
from blog.views import comments as comment_views
from blog.views import posts as post_views
from blog.views import tags as tag_views
from blog.views import core as core_views


urlpatterns = [
    path('posts/', post_views.PostListView.as_view(), name="posts_list"),
    path('post/<str:slug>/', post_views.PostDetail.as_view(), name="post_detail"),
    path('post/<str:slug>/comment/', comment_views.create_comment, name="comment_create_url"),
    path('post/<str:slug>/<int:pk>/reply/', comment_views.create_reply, name="reply_create_url"),
    path('posts/create/', post_views.PostCreate.as_view(), name="post_create"),
    path('post/<str:slug>/update/', post_views.PostUpdate.as_view(), name="post_update"),
    # path('post/<str:slug>/delete/', PostDelete.as_view(), name="post_delete"),
    path('post/new-delete/<int:post_id>/', post_views.PostDeleteView.as_view(), name="post_new_delete"),
    path('post/<int:post_id>/like/', post_views.LikePost.as_view(), name="like_post"),
    # path('post/<int:post_id>/dislike/', post_views.DislikePost.as_view(), name="dislike_post"),
    path('post/<int:post_id>/save/', post_views.SavePost.as_view(), name="save_post"),
    # path('post/<int:post_id>/unsaved/', post_views.UnsavedPost.as_view(), name="unsave_post"),
    path('tags/', tag_views.tags, name="tags"),
    path('tag/<str:slug>/', tag_views.TagDetail.as_view(), name="tag_detail"),
    path('tags/create/', tag_views.TagCreate.as_view(), name="tag_create"),
    path('tag/<str:slug>/update/', tag_views.TagUpdate.as_view(), name="tag_update"),
    # path('tag/<str:slug>/delete/', TagDelete.as_view(), name="tag_delete"),
    path('tag/new-delete/<int:tag_id>/', tag_views.TagDeleteView.as_view(), name="tag_new_delete"),
]
