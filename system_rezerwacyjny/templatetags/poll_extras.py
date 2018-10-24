from django import template
from system_rezerwacyjny.models import Sala, Reservation
register = template.Library()

@register.filter(name='reserve')
def reservation_today(id_sali_id, date):
    reserve = Reservation.objects.filter(id_sali_id=id_sali_id, date=date)
    if len(reserve) > 0:
        return 'Zajete'
    else:
        return 'Wolne'

@register.filter(name='date')
def reservation_today(id_sali_id, date):
    return date