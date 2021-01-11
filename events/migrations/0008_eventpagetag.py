# Generated by Django 3.1.4 on 2021-01-09 20:10

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('events', '0007_auto_20210109_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_tags', to='events.eventpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_eventpagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
