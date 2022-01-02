from django.contrib import admin

from .models import reportData, orders_done
from django.contrib.auth.models import Group
# Register your models here.

class reportAdmin(admin.ModelAdmin):
    list_display = ('name', 'cateogry')
    list_filter = ('cateogry',)

admin.site.site_header = 'Work Order Dashboard'

admin.site.register(reportData, reportAdmin)
admin.site.unregister(Group)


