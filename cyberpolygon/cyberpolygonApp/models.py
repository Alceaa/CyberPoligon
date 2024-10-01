from unittest.mock import mock_open

from django.contrib.auth.models import AbstractUser
import jsonfield
from django.urls import reverse
from django.db import models
from django.db.models import Model, OneToOneField


class User(AbstractUser):
    user_data = jsonfield.JSONField()
    id_role = models.ManyToManyField('Role')
    id_team = models.ManyToManyField('Team')

class Post(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    author = models.ForeignKey(User,
    on_delete=models.CASCADE,
    related_name='blog_posts')
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])

class Role(models.Model):
    role_name = models.TextField(max_length=256)
    description = models.TextField()

class Category(models.Model):
    name = models.TextField(max_length=256)

class Task(models.Model):
    id = models.AutoField(primary_key = True, db_index=True)
    title = models.TextField(max_length=256)
    description = models.TextField()
    points = models.IntegerField
    flag = models.TextField(max_length=256)
    is_active = models.BooleanField()
    created_at = models.DateField()

class Comments(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    task_id = models.ForeignKey('Task',  on_delete=models.PROTECT)
    user_id = models.ForeignKey('User',  on_delete=models.PROTECT)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.IntegerField()

class UserAvatar(models.Model):
    user_id = OneToOneField('User', on_delete=models.PROTECT)
    image_path = models.TextField(max_length=1024)
    image_hash = models.TextField(max_length=1024)
    created_at = models.DateField()

class TaskCategory(models.Model):
    task_id = models.ManyToManyField('Task')
    category_id = models.ManyToManyField('Category')

class Submission(models.Model):
    user_id= models.ManyToManyField('User')
    task_id= models.ForeignKey('Task', on_delete=models.PROTECT)
    flag_submitted=models.TextField(max_length=256)
    is_correct= models.BooleanField()
    submission_time= models.TimeField()

class Team(models.Model):
    name = models.TextField(max_length=256)
    created_at = models.DateField

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
# Create your models here.
