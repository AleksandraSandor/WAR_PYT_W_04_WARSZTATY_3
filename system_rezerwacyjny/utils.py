from calendar import HTMLCalendar
from datetime import datetime, timedelta
from system_rezerwacyjny.models import Reservation



class MyCalendar(HTMLCalendar):
    def __init__(self, room_id,  month=None, year=None):
        super().__init__(firstweekday=0)
        self.room_id = room_id
        self.year = year
        self.month = month

    def formatday(self, day, events):
        cssclass = self.cssclasses[events]
        print(datetime.now())
        events = Reservation.objects.filter(date__year=self.room_id, date__month=self.month, id_sali=self.year)
        notes = events.filter(date__day=day, id_sali=self.year)
        d = ''
        form = ''
        for note in notes:
            if note.note !="":
                d += f'<li> {note.note} </li>'
            else:
                d += f'<li> Zarezerwowana </li>'
        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        else:
            if f'{datetime.today().year}-{datetime.today().month}-{datetime.today().day}' == f'{self.room_id}-{self.month}-{day}':
                cssclass += ' today'
            if d != "":
                cssclass += ' reserved'
            if d == '':
                form += f'''<form method="POST">
                <input type="text" name="notes_{day}">
                <button value="{self.room_id}-{self.month}-{day}" name="date" >Zarezerwuj</button>
                <form>'''
            return f'<td class="{cssclass}">{day}<ul>{d}</ul>{form}</td>'
