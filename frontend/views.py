from django.shortcuts import render

# Create your views here.

def index(request, *args, **kwargs):
    print("Entrando en index react")
    return render(request, 'frontend/index.html')
