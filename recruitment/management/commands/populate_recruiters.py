from django.core.management import BaseCommand
from faker import Faker
from recruitment.models import Recruiter


def create_recruiters():
    fake = Faker("en_GB")
    for i in range(1, 10):
        Recruiter.objects.create(first_name=fake.first_name(), last_name=fake.last_name())


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_recruiters()
        self.stdout.write(self.style.SUCCESS("Successfully created Recruiters"))
