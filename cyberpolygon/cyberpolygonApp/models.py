from django.contrib.auth.models import AbstractUser
import jsonfield
from django.db import models
from django.db.models import Model, OneToOneField


class User(AbstractUser):
    user_data = jsonfield.JSONField()
    id_role = models.ForeignKey('Role', on_delete=models.PROTECT)

class Role(models.Model):
    role_name = models.TextField(max_length=50)
    description = models.TextField()

class Category(models.Model):
    name = models.TextField(max_length=50)

class Task(models.Model):
    id = models.AutoField(primary_key = True, db_index=True)
    title = models.TextField(max_length=100)
    description = models.TextField()
    points = models.IntegerField
    flag = models.TextField(max_length=100)
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
    image_path = models.TextField(max_length=255)
    image_hash = models.TextField(max_length=255)
    created_at = models.DateField()
# Create your models here.
