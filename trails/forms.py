from django import forms
from django.forms import ModelForm
from .models import Works 

class Works_upload_form(ModelForm):
	class Meta:
		model = Works
		fields = ['street_name', 'file_name', 'works_file']		

