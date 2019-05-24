from django.contrib import admin
from .models import Profile,Image,Comment
# Register your models here.
class picturesAdmin(admin.ModelAdmin):
    filter_horizontal =('Profiles',)

admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)


