from django.contrib import admin
from .models import Profile, Person, Dashboard_news, Works, Documents

admin.site.register(Profile)
admin.site.register(Person)
admin.site.register(Works)
admin.site.register(Dashboard_news)
admin.site.register(Documents)
# Register your models here.
