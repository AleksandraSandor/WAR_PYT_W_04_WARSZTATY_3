from calendar import HTMLCalendar
from datetime import date
from system_rezerwacyjny.models import Reservation



class MyCalendar(HTMLCalendar):
    def __init__(self, room_id):
        super().__init__(firstweekday=0)
        self.room_id = room_id

    def formatday(self, day, weekday):
        year = date.today().year
        month = date.today().month
        cssclass = self.cssclasses[weekday]
        notes = Reservation.objects.filter(date__day=day, id_sali=self.room_id)
        d = ''
        for note in notes:
            d += f'<li> {note.note} </li>'
        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        if d == '':
            d += f'</br><a href="#" onclick="overlay()">Zarezerwuj</a>'
            return f'<td class="{cssclass}">{day}{d}</td>'
        elif day != 0:
            if date.today() == date(year, month, day):
                cssclass += ' today'
            if d != "Zarezerwuj":
                cssclass += ' reserved'
            return f'<td class="{cssclass}">{day}{d}</td>'
        else:
            return f'<td class="{cssclass}">{day}{d}</td>'
