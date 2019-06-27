from django.urls import path
from .views import PostRudView, PostAPIView, CommentAPIView, CommentRudView, ReplyCommentAPIView, ReplyCommentRudView

urlpatterns =[
    path('api/post/<int:id>/', PostRudView.as_view(), name='post-rud'),
    path('api/post/', PostAPIView.as_view(), name='post-create'),
    path('api/comment/<int:id>/', CommentRudView.as_view(), name='comment-rud'),
    path('api/comment/', CommentAPIView.as_view(), name='comment-create'),
    path('api/replycomment/<int:id>/', ReplyCommentRudView.as_view(), name='replycomment-rud'),
    path('api/replycomment/', ReplyCommentAPIView.as_view(), name='replycomment-create'),
]