# Generated by Django 4.0 on 2022-03-26 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_options'),
        ('car', '0004_companycar'),
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('action', models.CharField(max_length=150)),
                ('message', models.CharField(max_length=255)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='messages', to='car.car')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='messages', to='core.user')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]