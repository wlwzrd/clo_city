
from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from sites.models import SiteCategory as Category, Neighborhood, Site as Commerce



def home(request):
    template = loader.get_template('index.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))
    
def neighborhoods(request, id):
    template = loader.get_template('neighborhood.html')
    context = {
        "neighborhoods" :Neighborhood.objects.filter(location__pk=id),
        "commune" : id
    }
    return HttpResponse(template.render(context, request))
def commerces(request, id, neighborhood):
    template = loader.get_template('commerces.html')
    categories = Commerce.objects.filter(neighborhood = neighborhood).values_list("category__pk", flat=True).distinct()
    categories = Category.objects.filter(pk__in = categories)
    context = {
        "commerces" : Commerce.objects.filter( neighborhood__id= neighborhood),
        "categories" : categories,
        "commune" : id
    }
    return HttpResponse(template.render(context, request))