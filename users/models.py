from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

from blog.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, unique=True)
    image = models.ImageField(default='default.jpg', blank=True, null=True, upload_to='profile_pics')
    #posts = models.ManyToManyField(Post, null=True, blank=True, related_name='user_posts')

    def get_profile_url(self, pk):
        return reverse('profile', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.username} Profile'
