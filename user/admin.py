from django.contrib import admin
from user.models import *

# Register your models here.
class signupAdmin(admin.ModelAdmin):
    list_display=['username','password','email','first_name','last_name']
class filefieldAdmin(admin.ModelAdmin):
    list_display=['choosefile']

admin.site.register(signup,signupAdmin)
admin.site.register(filefield,filefieldAdmin)
