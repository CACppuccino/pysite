from django.contrib import admin
from .models import lost_street, ls_gallery, ls_comments
# Register your models here.

admin.site.register(lost_street)
admin.site.register(ls_gallery)
admin.site.register(ls_comments)
