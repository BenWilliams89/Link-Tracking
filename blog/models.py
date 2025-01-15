from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here. Everytime i change/update the model make a migration

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_tag = models.CharField(unique=True, max_length=200,)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]
    
    def __str__(self):
        return self.title + '|' +str(self.author)

# another way to write the above is:

#def __str__(self):
#   return self.title + '|' + str(self.author) - this appears in the admin site

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="blog_comments"
    )
    author = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"