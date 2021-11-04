from django.core.management import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Creates a user admin"

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help="username of the admin")
        parser.add_argument('password', type=str, help="username of the admin")

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        try:
            User.objects.get(username=username)
            self.stdout.write(self.style.SUCCESS('Admin already exists'))
        except User.DoesNotExist:
            User.objects.create_superuser(username, password)
            self.stdout.write(self.style.SUCCESS('Admin with username {} created successfully'.format(username)))



