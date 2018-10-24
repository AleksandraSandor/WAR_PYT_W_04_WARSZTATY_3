from calendar import HTMLCalendar


class MyCalendar(HTMLCalendar):
    def formatday(self, day, weekday, data="Wolna"):
        if day == 0:
            return '<td class="noday">&nbsp;</td>'

        else:
            return f'<td class="{self.cssclasses[weekday]}">{day}{data} </td>'
