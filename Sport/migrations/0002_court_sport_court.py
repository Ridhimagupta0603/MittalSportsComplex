# Generated by Django 4.1 on 2022-09-02 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court_name', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='sport',
            name='court',
            field=models.ManyToManyField(null=True, to='Sport.court'),
        ),
    ]
