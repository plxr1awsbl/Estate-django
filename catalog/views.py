from django.shortcuts import render
from .models import Property

# Create your views here.
def catalog(request):
    
    properties = Property.objects.all().prefetch_related('images')
    
    return render(request, 'catalog/catalog.html', context={'properties': properties})

def propert(request, prop_slug):
    
    return render(request, 'catalog/details.html')