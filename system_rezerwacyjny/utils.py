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
        form = ''
        for note in notes:
            d += f'<li> {note.note} </li>'
        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        else:
            if date.today() == date(year, month, day):
                cssclass += ' today'
            if d != "":
                cssclass += ' reserved'
            if d == '':
                form += f'''</br><form method="POST">
                <input type="text" name="notes_{day}">
                <button value="{year}-{month}-{day}" name="date" >Zarezerwuj</button>
                <form>'''
            return f'<td class="{cssclass}">{day}{d}{form}</td>'

