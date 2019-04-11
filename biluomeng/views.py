from django.shortcuts import render
from datetime import datetime

def index(request):
    context= {}
    return render(request, 'index.html',context)