from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display_view(request):
    return HttpResponse('<h1>Shri Ganesh Thanks</h1>')
