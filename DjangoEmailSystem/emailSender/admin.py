from django.contrib import admin
from .models import Event, Employee, EmailTemplate, EmailLog

admin.site.register(Event)
admin.site.register(Employee)
admin.site.register(EmailTemplate)
admin.site.register(EmailLog)
