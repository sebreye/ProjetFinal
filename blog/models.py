from django.db import models
from users.models import Users
# Create your models here.

class category_blog(models.Model):
    name = models.CharField(max_length=200)
    def get_article_count(self):
        return blog.objects.filter(catblog=self).count()
    def get_articles(self):
        return blog.objects.filter(catblog=self)
    def __str__(self):
        return self.name
class tag_blog(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    description = models.TextField()
    catblog = models.ForeignKey(category_blog, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        username = self.user.username if self.user else 'Anonymous'
        return f"Comment by {username} on {self.blog.title}"