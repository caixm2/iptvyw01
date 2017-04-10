from django.contrib import admin
from .models import Thwsheji, Tztesheji

# Register your models here. 
class ThwshejiAdmin(admin.ModelAdmin):
    list_display = ('quju', 'jiedian', 'jdname', 'sjkyll','sjjdll','sjbf',
    'sjepgbf','sjdbkj')

class TzteshejiAdmin(admin.ModelAdmin):
    list_display = ('nodename', 'wgname', 'epggroupname', 'sjkyll', 'sjjdll',
        'sjhmsbf', 'sjepgbf', 'sjdbkj', 'nodeid', 'clusterid', 'clustername')

admin.site.register(Thwsheji, ThwshejiAdmin)

admin.site.register(Tztesheji, TzteshejiAdmin)