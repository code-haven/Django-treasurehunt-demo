from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'treasurehunt/treasurehunt_index.html')