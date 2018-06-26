from django.contrib import admin
from .models import doc_street, doc_permit_street, doc_building, doc_permit_building
# Register your models here.

admin.site.register(doc_street)
admin.site.register(doc_permit_street)
admin.site.register(doc_building)
admin.site.register(doc_permit_building)
