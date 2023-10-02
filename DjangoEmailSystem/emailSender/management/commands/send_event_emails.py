import datetime
from dateutils import relativedelta
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from ...models import Event, EmailTemplate, EmailLog

class Command(BaseCommand):
    help = 'Send event emails'

    def handle(self, *args, **kwargs):
        current_date = datetime.date.today()
        events = Event.objects.filter(event_date__month=current_date.month, event_date__day=current_date.day)

        for event in events:
            try:
                email_template = EmailTemplate.objects.get(event_type=event.event_type)
                subject = f"Happy {event.event_type}!"
                message = email_template.template_content.format(
                    employee_name=event.employee.name,
                    event_date=event.event_date
                )
                if event.event_type.lower() == "work anniversary":
                    anniversary = relativedelta(current_date, event.event_date).years
                    message = message.replace("anniversary_year_dynamic", str(anniversary))
                message = message.replace("Dear,", f"Dear {event.employee.name},")
                send_mail(subject, message, 'sender_email@example.com', [event.employee.email])
                EmailLog.objects.create(
                    employee=event.employee,
                    event=event,
                    sent_status=True
                )
            except Exception as e:
                EmailLog.objects.create(
                    employee=event.employee,
                    event=event,
                    sent_status=False,
                    error_message=str(e)
                )
