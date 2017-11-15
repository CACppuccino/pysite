from __future__ import unicode_literals
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

class vsr_Allbuildings(models.Model):
    primarykey = models.TextField(db_column='PrimaryKey', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    streetname = models.TextField(db_column='StreetName', unique=True)#ForeignKey('vsr_Streets', on_delete = models.CASCADE, db_index=False)  # Field name made lowercase. This field type is a guess.
    streetno = models.FloatField(db_column='StreetNo', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buildingname = models.TextField(db_column='BuildingName', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    buildingpix = models.TextField(db_column='BuildingPix', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pixcaption = models.TextField(db_column='PixCaption', blank=True, null=True)  # Field name made lowercase.
    builddate = models.TextField(db_column='BuildDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    demolishdate = models.TextField(db_column='DemolishDate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    architect = models.TextField(db_column='Architect', blank=True, null=True)  # Field name made lowercase.
    builder = models.TextField(db_column='Builder', blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='Info', blank=True, null=True)  # Field name made lowercase.
    links = models.TextField(db_column='Links', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AllBuildings'


class vsr_Streets(models.Model):
    name = models.TextField(db_column='Name', unique=True, blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    link = models.TextField(db_column='Link', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    streetpix = models.TextField(db_column='StreetPix', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    streetpix_caption = models.TextField(db_column='StreetPix Caption', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Streets'
# Create your models here.

