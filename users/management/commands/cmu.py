from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='iiiskhakov1990@mail.com',
            first_name='Admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=False,
        )

        user.set_password('123456')
        user.save()
