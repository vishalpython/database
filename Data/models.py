from django.db import models
import datetime

# Create your models here.
class Users(models.Model):
    #id = models.IntegerField(primary_key=True,null=False)
    username=models.CharField(max_length=225,unique=True,null=False)
    created_at = models.TimeField(auto_now_add=True)


class Photos(models.Model):
    #id = models.IntegerField(primary_key=True)
    image_url = models.CharField(max_length=225,null=False)
    user = models.ForeignKey(Users,on_delete = models.CASCADE)
    created_at = models.TimeField(default=datetime.time(16, 00),null=True)


class Comments(models.Model):
    comment_text = models.CharField(max_length=225,null=False)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    photo = models.ForeignKey(Photos,on_delete = models.CASCADE)
    created_at = models.TimeField(default=datetime.time(16, 00),null=True)
class Likes(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    photo = models.ForeignKey(Photos,on_delete=models.CASCADE)
    created_at = models.TimeField(default=datetime.time(16, 00),null=True)


class Follows(models.Model):
    follower_id = models.ManyToManyField(Users,related_name='user')
    followee_id = models.ManyToManyField(Users)
    created_at = models.TimeField(default=datetime.time(16, 00),null=True)
