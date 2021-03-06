# Generated by Django 3.0.6 on 2022-01-31 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConferenceRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('capacity', models.PositiveIntegerField()),
                ('projector_availability', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RoomReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comment', models.TextField(null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Booking_app.ConferenceRoom')),
            ],
            options={
                'unique_together': {('room_id', 'date')},
            },
        ),
    ]
