from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user = User.objects.create(
            phone='79121222223',
            email='admin@admin.com',
            first_name='Admin',
            last_name='Adminov',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()
        print("Superuser was created!")
