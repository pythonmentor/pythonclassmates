# Generated by Django 3.1.4 on 2021-01-08 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20201230_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='start',
            field=models.DateField(null=True, verbose_name='start'),
        ),
    ]
