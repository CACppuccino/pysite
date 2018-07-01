from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = 'usr/avatar', default = 'usr/avatar/default.jpg')
    organization = models.CharField(max_length=200, null=True, blank=True) # the institution/uni/school the user belongs to
    summary = models.TextField(null=True, blank=True) # the summary to introduce himself
