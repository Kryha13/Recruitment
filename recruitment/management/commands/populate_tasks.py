from django.core.management import BaseCommand
from faker import Faker
from recruitment.models import Task


def create_tasks():
    fake = Faker("en_GB")
    for i in range(1, 100):
        Task.objects.create(title=fake.company())


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_tasks()
        self.stdout.write(self.style.SUCCESS('Successfully created Tasks'))
