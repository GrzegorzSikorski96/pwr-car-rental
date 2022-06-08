# Generated by Django 4.0 on 2022-06-08 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_usercarpickupaddress'),
        ('car', '0007_scheduleservice_availability_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='schedules', to='core.user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='events', to='car.availability')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='events', to='schedule.schedule')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
