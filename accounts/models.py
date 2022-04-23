from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

import room
# Create your models here.


class Guest(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phoneNumber = PhoneNumberField(unique=True)

    def __str__(self):
        return str(self.user)

    def numOfBooking(self):
        return room.models.Booking.objects.filter(guest=self).count()

    def numOfDays(self):
        totalDay = 0
        bookings = room.models.Booking.objects.filter(guest=self)
        for b in bookings:
            day = b.endDate - b.startDate
            totalDay += int(day.days)

        return totalDay

    def numOfLastBookingDays(self):
        try:
            return int((room.models.Booking.objects.filter(guest=self).last().endDate - room.models.Booking.objects.filter(guest=self).last().startDate).days)
        except:
            return 0

    def currentRoom(self):
        booking = room.models.Booking.objects.filter(guest=self).last()
        return booking.roomNumber


class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phoneNumber = PhoneNumberField(unique=True)
    salary = models.FloatField()

    def __str__(self):
        return str(self.user)


class Task(models.Model):
    employee = models.ForeignKey(
        Employee,   null=True, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    description = models.TextField()

    def str(self):
        return str(self.employee)
