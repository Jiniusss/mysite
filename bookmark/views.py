from django.shortcuts import render
#from django.view.generic.list import ListView
from .models import Bookmark


# Create your views here.

def index(request):

    num_bookmarks = Bookmark.objects.all().count()
    context = {
        'num_bookmarks': num_bookmarks,


    }

    return render(request, 'index.html', context=context)