# Generated by Django 3.1.4 on 2020-12-30 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventpage',
            options={'verbose_name': 'Event Page', 'verbose_name_plural': 'Event Pages'},
        ),
        migrations.AlterModelOptions(
            name='eventspage',
            options={'verbose_name': 'Events Page', 'verbose_name_plural': 'Events Pages'},
        ),
    ]