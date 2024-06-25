from django.core.management.base import BaseCommand
from userauths.models import User, Profile

class Command(BaseCommand):
    help = 'Create profile for superuser'

    def handle(self, *args, **options):
        superuser = User.objects.filter(is_superuser=True).first()

        if superuser:
            # Check if superuser already has a profile
            if not hasattr(superuser, 'profile'):
                model=Profile(user=superuser, bio="Superuser", profile_picture=None)
                model.save()
                self.stdout.write(self.style.SUCCESS('Profile created for superuser'))
            else:
                self.stdout.write(self.style.WARNING('Superuser already has a profile'))
        else:
            self.stdout.write(self.style.ERROR('Superuser does not exist'))
