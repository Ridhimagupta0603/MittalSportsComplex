# Generated by Django 4.1 on 2022-09-02 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sport', '0004_remove_sport_court_sport_court'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='court',
        ),
        migrations.AddField(
            model_name='sport',
            name='court',
            field=models.ManyToManyField(to='Sport.court'),
        ),
    ]
