from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

from blog.models import Post
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True, unique=True)
    post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', blank=True, null=True, upload_to='profile_pics')

    def get_profile_url(self):
        return reverse('profile', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.user.username} Profile'
