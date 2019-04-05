from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class Candidate(models.Model):
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Grade(models.Model):
    value = models.DecimalField(max_digits=2, decimal_places=1)
    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='candidates')
    recruiter = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.candidate} - {self.value}'

