from django.shortcuts import render

from .models import Topic

# Create your views here.
def index(request):
    """The home page for Learning app"""
    return render(request, 'learning_apps/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_apps/topics.html', context)