from django.contrib import admin

# Register your models here.

from .models import Contact,MapUserContact,Profile

admin.site.register(Contact)
admin.site.register(MapUserContact)
admin.site.register(Profile)
