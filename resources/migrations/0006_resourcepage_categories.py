# Generated by Django 3.1.4 on 2021-01-12 22:56

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0011_auto_20210110_1920'),
        ('resources', '0005_resourcepage_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcepage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='streams.Category'),
        ),
    ]