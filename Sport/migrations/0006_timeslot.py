# Generated by Django 4.1 on 2022-09-02 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sport', '0005_remove_sport_court_sport_court'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromtime', models.TimeField()),
                ('totime', models.TimeField()),
            ],
        ),
    ]
