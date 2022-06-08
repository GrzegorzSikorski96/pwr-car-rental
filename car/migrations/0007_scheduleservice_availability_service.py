# Generated by Django 4.0 on 2022-06-08 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_alter_availability_end'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ended_at', models.DateTimeField(null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='scheduled_services', to='car.car')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='availability',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='availabilities', to='car.scheduleservice'),
        ),
    ]
