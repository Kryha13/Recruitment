from django.core.management import BaseCommand
from faker import Faker
from recruitment.models import Candidate


def create_candidates():
    fake = Faker("en_GB")
    for i in range(1, 50):
        Candidate.objects.create(first_name=fake.first_name(), last_name=fake.last_name())


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_candidates()
        self.stdout.write(self.style.SUCCESS("Successfully created Candidates"))
