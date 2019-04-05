from django.contrib import admin
from recruitment.models import Candidate, Grade, Task

# Register your models here.

admin.site.register(Candidate)
admin.site.register(Task)
admin.site.register(Grade)
