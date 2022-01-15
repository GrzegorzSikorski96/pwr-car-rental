# Generated by Django 4.0 on 2022-01-11 19:46

from django.db import migrations, models
import django.utils.timezone
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.CharField(max_length=50, null=True)),
                ('horsepower', models.PositiveIntegerField()),
                ('fuel_type', models.CharField(choices=[('gas', 'Gas'), ('diesel', 'Diesel'), ('electric', 'Electric')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=80)),
                ('model', models.CharField(max_length=80)),
                ('mileage', models.PositiveIntegerField(default=1000)),
                ('production_date', models.DateField()),
                ('air_conditioning', models.BooleanField(default=False)),
                ('transmission_type', models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic')], max_length=15)),
                ('body_type', models.CharField(choices=[('micro', 'Micro'), ('sedan', 'Sedan'), ('suv', 'Suv'), ('hatchback', 'Hatchback'), ('roadster', 'Roadster'), ('pickup', 'Pickup'), ('van', 'Van'), ('coupe', 'Coupe'), ('supercar', 'Supercar'), ('camper', 'Camper'), ('cabriolet', 'Cabriolet'), ('minivan', 'Minivan')], max_length=20)),
                ('drivetrain_type', models.CharField(choices=[('all wheel drive', 'All wheel drive'), ('four wheel drive', 'Four wheel drive'), ('front wheel drive', 'Front wheel drive'), ('rear wheel drive', 'Rear wheel drive')], max_length=25)),
                ('daily_rent_price', models.PositiveIntegerField()),
                ('weekly_rent_price', models.PositiveIntegerField()),
                ('monthly_rent_price', models.PositiveIntegerField()),
                ('seats', models.PositiveIntegerField()),
                ('trunk_volume', models.PositiveIntegerField()),
                ('service_mileage_interval', models.PositiveIntegerField(default=15000)),
                ('insured_date', models.DateField(default=django.utils.timezone.now)),
                ('technical_overview_date', models.DateField(default=django.utils.timezone.now)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cars', to='car.engine')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_cars', to='core.user')),
            ],
        ),
    ]
