from django.core.management import BaseCommand

from courses.models import Payment
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        payment = Payment.objects.create(
            user=User.objects.filter(email='admin@sky.pro'),
            # pay_date = ,
            course=5,
            # lesson = ,
            sum=128,
            method=('cash', 'cash')
        )

        payment.save()
