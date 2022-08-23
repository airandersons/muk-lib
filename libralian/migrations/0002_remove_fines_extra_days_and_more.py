# Generated by Django 4.0.5 on 2022-08-22 14:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libralian', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fines',
            name='extra_days',
        ),
        migrations.AlterField(
            model_name='fines',
            name='actual_return_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 14, 7, 53, 8021, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fines',
            name='date_taken',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 14, 7, 53, 8021, tzinfo=utc), editable=False),
        ),
    ]
