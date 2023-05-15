from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):    
    return render(request, 'index.html')       

def benchmarking(request):    
    return render(request, 'benchmarking.html')

def dashboard(request):    
    return render(request, 'dashboard.html')

def data_analytics(request):    
    return render(request, 'data_analytics.html')

def shoes(request):    
    return render(request, 'shoes.html')

