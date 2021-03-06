# Generated by Django 3.1 on 2020-09-12 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft_number', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_reference', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=4, max_digits=18)),
                ('take_off_point', models.CharField(max_length=150)),
                ('take_off_time', models.DateTimeField()),
                ('destination', models.CharField(max_length=150)),
                ('flight_class', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=50, unique=True)),
                ('take_off_point', models.CharField(max_length=150)),
                ('take_off_time', models.DateTimeField()),
                ('destination', models.CharField(max_length=150)),
                ('price', models.DecimalField(decimal_places=4, max_digits=18)),
                ('flight_class', models.CharField(max_length=20)),
                ('aircraft', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.aircraft')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.flight'),
        ),
    ]
