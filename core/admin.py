from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Projects)
admin.site.register(Developers)
admin.site.register(InfoNotifications)
admin.site.register(WarningNotifications)

