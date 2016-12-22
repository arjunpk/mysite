from django.contrib import admin

# Register your models here.
from .models import Categories, Countries, States, Cities, ZipCodes, Profile

admin.site.register(Categories)
admin.site.register(Countries)
admin.site.register(States)
admin.site.register(Cities)
admin.site.register(ZipCodes)
admin.site.register(Profile)

