from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from system_rezerwacyjny  import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404,redirect

from system_rezerwacyjny.forms import PostForm
from system_rezerwacyjny.models import Sala


def new_room(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('new_room')
    else:
        form = PostForm()
    return render(request, 'system_rezerwacyjny/add.html', {'form': form})


def modify_room(request,id):
    pass

def delete_room(request, id):
    pass

def single_room(request,id):
    pass


def all_rooms(request):
    rooms = Sala.objects.all()
    return render(request, 'system_rezerwacyjny/sale.html', {'rooms':rooms})
