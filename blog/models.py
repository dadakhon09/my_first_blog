from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, db_index=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    content = models.TextField(null=True, db_index=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    created_on = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='author_posts')
    image = models.ImageField(default="default_post.jpg", blank=True, null=True, upload_to='post_pics')

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('post_update', kwargs={'slug': self.slug})

    # def get_delete_url(self):
    #     return reverse('post_delete', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('tag_update', kwargs={'slug': self.slug})

    # def get_delete_url(self):
    #     return reverse('tag_delete', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(default='comment', max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post.title}-{self.user.username}'
