from django.contrib import admin
from .models import doc_street, doc_building
# Register your models here.

admin.site.register(doc_street)
admin.site.register(doc_building)
