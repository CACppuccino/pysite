from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class doc_street(models.Model):
    name = models.CharField(max_length = 100)
    cover = models.ImageField(upload_to = 'stdoc/cover')
    intro = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class doc_permit_street(models.Model):
    name = models.CharField(max_length = 100)
    sid = models.ForeignKey(doc_street, on_delete = models.CASCADE)

class doc_building(models.Model):
    stname = models.ForeignKey(doc_permit_street, related_name='buildings', on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    cover = models.ImageField(upload_to = 'stdoc/bcover')
    intro = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)


class doc_permit_building(models.Model):
    name = models.CharField(max_length = 100)
    bid = models.ForeignKey(doc_building, on_delete = models.CASCADE)
