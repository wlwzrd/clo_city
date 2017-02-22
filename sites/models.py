from __future__ import unicode_literals

from django.db import models

# Create your models here.
 
class Commune(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=600)
    class Meta:
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'
    def __unicode__(self):
        return self.name

class Neighborhood(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    location = models.ForeignKey(Commune, null=False)
    class Meta:
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrios'
    def __unicode__(self):
        return self.name

class SiteCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural =  'Categorias'
    def __unicode__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=600)
    address = models.CharField(max_length=200,default="Av 3N")
    phone = models.CharField(max_length=10,default="1234567890")
    category = models.ForeignKey(SiteCategory, null=False)
    neighborhood = models.ManyToManyField(Neighborhood)
    class Meta:
        verbose_name = 'Sitio'
        verbose_name_plural = 'Sitios'
    def __unicode__(self):
        return self.name

class SiteImages(models.Model):
    site = models.ForeignKey(Site)
    image = models.ImageField(upload_to='images/sites/')
    class Meta:
        verbose_name = 'Imagen Sitio'
        verbose_name_plural = 'Imagenes Sitio'
    def __unicode__(self):
        return u'Site: %s -  ImageCod: %s'%(self.site.name,self.pk)
