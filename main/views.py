from django.shortcuts import render
from catalog.models import Property

# Create your views here.
def index(request):
    
    return render(request, 'main/index.html')