from django.urls import path
from .views import PostRudView, PostAPIView

urlpatterns =[
    path('api/post/<int:id>/', PostRudView.as_view(), name='post-rud'),
    path('api/post/', PostAPIView.as_view(), name='post-create'),
]