from django.db import models


class ConferenceRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.PositiveIntegerField()
    projector_availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class RoomReservation(models.Model):
    room = models.ForeignKey(ConferenceRoom, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)

    def __str__(self):
        return str(self.date) + " | " + str(self.room_id)

    class Meta:
        unique_together = ('room_id', 'date',)
