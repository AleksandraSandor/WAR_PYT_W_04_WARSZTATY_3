from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404,redirect
from system_rezerwacyjny.forms import PostForm, ReservationForm
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
    pass

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
        return HttpResponseRedirect(reverse('all_rooms'))
    else:
        return render(request, 'system_rezerwacyjny/reservation.html',
                      {'room': room, "cal": mark_safe(html_cal), "month": month, "year": year, "day": day})
