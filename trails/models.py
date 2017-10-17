from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

class Profile(models.Model):
	user = models.OneToOneField(get_user_model(), on_delete = models.CASCADE)
	headImg = models.ImageField(upload_to = 'headImg/')
	Introduction  = models.CharField(max_length = 140)

class Person(models.Model):
	first_name = models.CharField(max_length=30, db_tablespace = "person")
	last_name  = models.CharField(max_length = 30, db_tablespace = "person")

	class Meta:
		db_tablespace = "person"

class Works(models.Model):
	street_name = models.CharField(max_length=50, db_tablespace = "works")
	file_name = models.CharField(max_length=50, db_tablespace = "works")
	works_file = models.FileField(db_tablespace = "works")
	
	class Meta:
		db_tablespace = "works"

class Documents(models.Model):
	title = models.CharField(max_length=50)
	location  = models.TextField()
	
	class Meta:
		db_tablespace = "doc"
class Dashboard_news(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete = models.PROTECT)
	action = models.TextField()
	time = models.DateTimeField(auto_now_add = True)
# Create your models here.
