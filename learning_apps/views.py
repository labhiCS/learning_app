from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Learning app"""
    return render(request, 'learning_apps/index.html')