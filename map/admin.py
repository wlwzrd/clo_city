from django.contrib import admin
from map.models import *

# Register your models here.

admin.site.register(Commune)
admin.site.register(Neighborhood)
admin.site.register(CommerceCategory)

class CommerceAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ('name', 'category', 'neighborhood')
    list_filter = ('category', 'neighborhood')

admin.site.register(Commerce, CommerceAdmin)