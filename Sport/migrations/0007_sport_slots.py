# Generated by Django 4.1 on 2022-09-02 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sport', '0006_timeslot'),
    ]

    operations = [
        migrations.AddField(
            model_name='sport',
            name='slots',
            field=models.ManyToManyField(to='Sport.timeslot'),
        ),
    ]
