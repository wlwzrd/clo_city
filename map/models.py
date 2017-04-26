from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Commune(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='images/communes/')
    class Meta:
        verbose_name = 'Commune'
        verbose_name_plural = 'Communes'
    def __unicode__(self):
        return self.name


class Neighborhood(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    commune = models.ForeignKey(Commune)
    class Meta:
        verbose_name = 'Neighborhood'
        verbose_name_plural = 'Neighborhoods'
    def __unicode__(self):
        return self.name


class CommerceCategory(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural =  'Categories'
    def __unicode__(self):
        return self.name

class Commerce(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    category = models.ForeignKey(CommerceCategory)
    neighborhood = models.ForeignKey(Neighborhood)
    image = models.ImageField(upload_to='images/commerces/')
    class Meta:
        verbose_name = 'Commerce'
        verbose_name_plural = 'Commerces'
    def __unicode__(self):
        return self.name
class CommerceImage(models.Model):
    name = models.TextField()
    image = models.ImageField(upload_to="images/commerces/",null = True, blank = True)
    commerce = models.ForeignKey(Commerce)
class SecondaryImage(models.Model):
    commerce = models.ForeignKey(Commerce, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/commerces/secondary/')
    
