from django.db import models
from django.utils import timezone
from django.urls import reverse 

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)


    def publish(self):
        # when we publish a blog post and it will take the current time and save that.
        # this method was created as  want to link to another button 
        self.published_date = timezone.now()
        self.save()
    
    
    # Post can have comments and we want to approve them so they can been seen under each blog post
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    # once you've created an instance of this post it returns post details. once submit it will go to the primary key you created 
    # once the post is done it will go back 
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    # string representation for for Post usually title makes sense 
    def __str__(self):
        return self.title 

# realted to post class 
class Comment(models.Model):
    # each comment will be connected to a blog post 
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=150)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    # comments will approved by useruser. once comment is done the user will go back to the list all posts 
    def get_absolute_url(self):
        return reverse('post_list')    

    def __str__(self):
        return self.text
