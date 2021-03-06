from django.contrib import admin
from .models import Commune, Neighborhood, SiteCategory, Site, SiteImages
# Register your models here.

admin.site.register(Commune)
admin.site.register(Neighborhood)
admin.site.register(SiteCategory)

class ImageInLine(admin.TabularInline):
    model = SiteImages
    extra = 3

class SiteAdmin(admin.ModelAdmin):
    fieldsets =[
        (None, {'fields':['name','description','address','phone']}),
        ('Asociaciones',{'fields':['category','neighborhood'],'classes':['collapse']}),
    ]
    inlines = [ImageInLine]
    search_fields = ['name']
    list_display = ('name','category')
    list_filter = ('category','neighborhood')

admin.site.register(Site,SiteAdmin)
admin.site.site_title = 'Santiago de Cali Comunas'
admin.site.site_header = 'Administracion'
