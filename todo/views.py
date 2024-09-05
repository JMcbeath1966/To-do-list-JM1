from django.shortcuts import render
from .models import Item


# Create your views here.


def get_todo_list(request):
    #return HttpResponse(request, 'todo/todo_list.html')
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
    