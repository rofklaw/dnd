from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User
# Create your models here.

class Post(models.Model):
	text = models.CharField(max_length=255)
	poster = models.ForeignKey(User, related_name = "posts")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	
class Comment(models.Model):
	text = models.CharField(max_length=255)
	poster = models.ForeignKey(User, related_name = "comments")
	post = models.ForeignKey(Post, related_name = "comments")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)