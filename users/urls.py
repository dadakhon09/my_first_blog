from django.contrib.auth import views as auth_views
from django.urls import path
from users.views import register, profile, update_profile, profile_list

urlpatterns = [
    path('register/', register, name="register"),
    path('profile/<int:pk>/', profile, name="profile"),
    path('update_profile/', update_profile, name="update_profile"),
    path('profile_list/', profile_list, name="profile_list"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
]
