# Generated by Django 4.1.1 on 2022-09-15 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_eventregister'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventregister',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event'),
        ),
    ]
