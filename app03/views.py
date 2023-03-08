from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def yogi(request):
    return HttpResponse('<h1> hai yogieswar</h1>')