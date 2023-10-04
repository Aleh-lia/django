from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

