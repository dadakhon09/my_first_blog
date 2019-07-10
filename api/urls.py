from django.urls import path
from .views import PostRudView, PostAPIView, CommentAPIView, CommentRudView, \
    ReplyCommentAPIView, ReplyCommentRudView, CommentCreateAPIView, ReplyCreateAPIView

urlpatterns =[
    path('api/post/<int:id>/', PostRudView.as_view(), name='post-rud'),
    path('api/post/', PostAPIView.as_view(), name='post-create'),
    path('api/comment/<int:id>/', CommentRudView.as_view(), name='comment-rud'),
    path('api/comment/', CommentAPIView.as_view(), name='comment-create'),
    # path('api/replycomment/<int:id>/', ReplyCommentRudView.as_view(), name='replycomment-rud'),
    path('api/replycomment/<int:com_id>/', ReplyCreateAPIView.as_view(), name='replycomment-create'),
    path('api/comment/create/<int:post_id>/', CommentCreateAPIView.as_view(), name='comment-create-new'),
]