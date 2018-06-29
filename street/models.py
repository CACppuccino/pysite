from django.db import models
from django.utils import timezone
import json
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
#from imagekit.processors import ResizeToFill

# Create your models here.

# class for the lost street
class lost_street(models.Model):
    name = models.CharField(max_length = 100)
    cover = models.ImageField(upload_to = 'loststreet/cover')
    intro = models.TextField(default = 'unknown')

    def __str__(self):
        return self.name

class ls_gallery(models.Model):
    sname = models.ForeignKey(lost_street, related_name='gallery', on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'loststreet/gallery')
    thumbnail = ImageSpecField(source = 'image', format = 'JPEG', options = {'quilty':80})

    def __str__(self):
        return json.dumps(dict(id=self.id, image = str(self.image), thumbnail = str(self.thumbnail))) 
        #return str(self.image)

class ls_comments(models.Model):
    sname = models.ForeignKey(lost_street, related_name='comments', on_delete = models.CASCADE)
    uname = models.ForeignKey(User, related_name='user', on_delete = models.CASCADE)
    time = models.DateTimeField(editable = False, default = timezone.now)
    content = models.TextField()
