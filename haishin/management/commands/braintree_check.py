from django.core.management.base import BaseCommand, CommandError
from haishin.models import *
import sendmails
from django.conf import settings

class Command(BaseCommand):

    """
    "authorization_expired"
    "authorized"
    "authorizing"
    "settlement_pending"
    "settlement_confirmed"
    "settlement_declined"
    "failed"
    "gateway_rejected"
    "processor_declined"
    "settled"
    "settling"
    "submitted_for_settlement"
    "voided"
    """

    def handle(self, *args, **options):

        disablecss = True
        sendmails.Email.set_configuration(settings.EMAIL_API_BASE_URL,settings.EMAIL_API_KEY, settings.EMAIL_FROM, disablecss)

        methods = PaymentMethod.objects.exclude(last_status__in=['settled','failed','gateway_rejected','processor_declined','voided'])
        for method in methods:
            previous_status = method.last_status
            self.stdout.write('Searchin status for %s. Previous: %s' % (method.job.id, previous_status))
            method.update_status()
            self.stdout.write('New status: %s' % (method.last_status))

            if method.last_status != previous_status:
                mail_sended = sendmails.Email.notify_payment_change(method.job,previous_status,method.last_status)

        self.stdout.write('Finished')