from django.db import models

# Create your models here.
class Sala(models.Model):
    name = models.CharField(max_length=128)
    capacity = models.IntegerField()
    is_projector = models.BooleanField(default=True)

    def __str__(self):
        return "{} {} {}".format(self.name, self.capacity, self.is_projector)


class Reservation(models.Model):
    date = models.DateField(null=True)
    id_sali = models.ForeignKey(Sala, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return "{} {} {}".format(self.date, self.id_sali, self.note)
