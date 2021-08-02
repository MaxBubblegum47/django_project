from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(models.Model):
    title = models.CharField(max_length=100)
    audio = models.FileField(default="cash.mp3")
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    singer = models.CharField(max_length=100, default="", blank=True)
    album = models.CharField(max_length=100, default="", blank=True)
    likes = models.ManyToManyField(User, related_name="blog_post")
    category = models.CharField(max_length=255, default="uncategorized", blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Report(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='report')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_report = models.BooleanField(default=True)

    def approve(self):
        self.approved_report = True
        self.save()

    def __str__(self):
        return self.text
