from django.shortcuts import render, get_object_or_404
from .models import Property

# Create your views here.
def catalog(request):
    
    properties = Property.objects.all()
    
    return render(request, 'catalog/catalog.html', context={'properties' : properties})

def propert(request, prop_slug):
    
    prop = get_object_or_404(Property, slug=prop_slug)
    
    return render(request, 'catalog/details.html', context={'property' : prop})