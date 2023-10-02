from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee, Event
from datetime import date

@receiver(post_save, sender=Employee)
def create_dob_event(sender, instance, created, **kwargs):
    if created:
        # Create an event for the employee's DOB
        Event.objects.create(
            event_type="Birthday",
            event_date=instance.dob,
            employee=instance,
        )

@receiver(post_save, sender=Employee)
def create_doj_event(sender, instance, created, **kwargs):
    if created:
        # Create an event for the employee's DOB
        Event.objects.create(
            event_type="Work Anniversary",
            event_date=instance.doj,
            employee=instance,
        )