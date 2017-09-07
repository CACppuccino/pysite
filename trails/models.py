from django.db import models

class Person(models.Model):
	first_name = models.CharField(max_length=30, db_tablespace = "person")
	last_name  = models.CharField(max_length = 30, db_tablespace = "person")

	class Meta:
		db_tablespace = "person"
# Create your models here.
