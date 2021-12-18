from django.contrib import admin
from vlog.models import *

# Register your models here.

class VlogAdmin(admin.ModelAdmin):
    list_display=['title','location','image','description']
    list_editable=['location','image','description']

admin.site.register(Vlog,VlogAdmin)
