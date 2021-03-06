# Generated by Django 2.2 on 2019-04-05 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=50)),
                ('last_name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=1, max_digits=2)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.Candidate')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recruitment.Task')),
            ],
        ),
    ]
