from django.shortcuts import render, get_object_or_404
from .models import Property

# Create your views here.
def catalog(request):
    
    properties = Property.objects.all()
    
    return render(request, 'catalog/catalog.html', context={'properties' : properties})

def propert(request, prop_slug):
    
    prop = get_object_or_404(Property, slug=prop_slug)
    image_list = prop.images.all()
    benefits = prop.benefits.all()
    
    return render(request, 'catalog/single-property.html', context={'property' : prop, 'images' : image_list, 'benefits': benefits})