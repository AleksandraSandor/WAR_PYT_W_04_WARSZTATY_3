from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404,redirect
from system_rezerwacyjny.forms import PostForm, SearchForm
from system_rezerwacyjny.models import Sala, Reservation
from system_rezerwacyjny.utils import MyCalendar
from datetime import datetime
from calendar import HTMLCalendar
from django.utils.safestring import mark_safe


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
    rooms = get_object_or_404(Sala, pk=id)
    date = Reservation.objects.filter(id_sali_id=id).order_by('date').filter(date__gte=datetime.today())
    return render(request, 'system_rezerwacyjny/single_room.html', {'rooms': rooms, 'date': date, 'month':datetime.now().month, 'day':datetime.now().day, 'year':datetime.now().year })

def all_rooms(request):
    if request.method == "POST":
        rooms = Sala.objects.all().order_by('id')
        date = request.POST.get('date')
        if date == '':
            return render(request, 'system_rezerwacyjny/sale.html', {'rooms':rooms, 'form':False})
        return render(request, 'system_rezerwacyjny/sale.html', {'rooms': rooms, 'form': True, 'date': date })
    else:
        rooms = Sala.objects.all().order_by('id')
        return render(request, 'system_rezerwacyjny/sale.html', {'rooms':rooms, 'form':False})

@csrf_exempt
def reservation(request, id, month=datetime.now().month, day=datetime.now().day, year=datetime.now().year):
    room = Sala.objects.get(pk=id)
    if month == 0:
        month = 12
        year -= 1
    if month == 13:
        month = 1
        year += 1

    cal = MyCalendar(year, month, room.id)
    html_cal = cal.formatmonth(year, month)
    if request.method == "POST":
        d = request.POST.get("date")
        day = str(d).split("-")[2]
        n = request.POST.get(f"notes_{day}")
        Reservation.objects.create(date=d, note=n, id_sali=room)
        return render(request, 'system_rezerwacyjny/reservation.html',
                      {'form':False, 'room': room})
    else:
        return render(request, 'system_rezerwacyjny/reservation.html',
                      {'room': room, "cal": mark_safe(html_cal), "month": month, "year": year, "day": day, 'form':True})


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            capacity = form.cleaned_data['capacity']
            is_projector = form.cleaned_data['is_projector']
            date = form.cleaned_data['date']
            if name:
                room_name = Sala.objects.filter(name__icontains=name)
            else:
                room_name = Sala.objects.all()

            if capacity:
                room_capacity = Sala.objects.filter(capacity__gte=capacity)
            else:
                room_capacity = Sala.objects.all()

            if is_projector:
                room_projector = Sala.objects.filter(is_projector=is_projector)
            else:
                room_projector = Sala.objects.all()
            rooms = room_name & room_capacity & room_projector

            if date:
                temp = []
                for room in rooms:
                    free_room = Reservation.objects.filter(date=date, id_sali_id=room)
                    if len(free_room) == 0:
                        temp.append(room)
            else:
                temp = rooms
            return render(request, 'system_rezerwacyjny/search.html', {'rooms': temp, 'get': True})
    else:
        form = SearchForm()
        return render(request, 'system_rezerwacyjny/search.html', {'get': False, 'form':form})
