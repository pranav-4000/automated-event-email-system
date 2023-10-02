from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    doj = models.DateField()
    dob = models.DateField()

class Event(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=255)
    event_date = models.DateField()

class EmailTemplate(models.Model):
    event_type = models.CharField(max_length=255, unique=True)
    template_content = models.TextField()

class EmailLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    sent_status = models.BooleanField()
    error_message = models.TextField()
    sent_datetime = models.DateTimeField(auto_now_add=True)
