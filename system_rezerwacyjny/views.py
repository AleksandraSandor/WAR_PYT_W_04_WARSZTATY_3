from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from system_rezerwacyjny import *
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
        msg_add = "Dodaj nową salę:"
    return render(request, 'system_rezerwacyjny/add.html', {"msg_add": msg_add, 'form': form})


def modify_room(request, id):
    post = get_object_or_404(Sala, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('all_rooms')
    else:
        form = PostForm(instance=post)
        msg_edit = "Zedytuj salę:"
    return render(request, 'system_rezerwacyjny/modify.html', {"msg_edit": msg_edit, 'form': form, 'room':post})


def delete_room(request, id):
    room_delete = Sala.objects.get(pk=id)
    room_delete.delete()
    return render(request, 'system_rezerwacyjny/delete.html', {"room_delete":room_delete})


def single_room(request,id):
    pass

def all_rooms(request):
    rooms = Sala.objects.all().order_by('id')
    return render(request, 'system_rezerwacyjny/sale.html', {'rooms':rooms})

