from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from blog.views.core import home
from users.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('', include('blog.urls')),
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    path('update_profile/', update_profile, name="update_profile"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
