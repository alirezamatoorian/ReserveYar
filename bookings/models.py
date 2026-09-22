from django.db import models
from resources.models import Resource
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.



class Booking(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING='pending','pending'
        CONFIRMED='confirmed','confirmed'
        CHECKED_IN='checked_in','checked_in'
        COMPLETED='completed','completed'
        CANCELLED='cancelled','cancelled'
        NO_SHOW='no_show','no_show'
        EXPIRED='expired','expired'
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE,related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='bookings')
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    checked_in_at=models.DateTimeField(blank=True, null=True)
    status=models.CharField(max_length=50,choices=StatusChoices, default=StatusChoices.PENDING)
    reminder_sent=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)


class WaitlistEntry(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE,related_name='waitlist_entries')
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='waitlist_entries')
    desired_start=models.DateTimeField()
    desired_end=models.DateTimeField()
    created_at=models.DateTimeField(auto_now_add=True)