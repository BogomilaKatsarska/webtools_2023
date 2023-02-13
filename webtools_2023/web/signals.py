from django.db.models import signals
from django.dispatch import receiver

from webtools_2023.web.models import Employee


@receiver(signals.post_save, sender=Employee)
def handle_employee_create(*args, **kwargs):
    print(args)
    print(kwargs)
