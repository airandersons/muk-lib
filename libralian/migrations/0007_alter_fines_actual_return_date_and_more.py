# Generated by Django 4.0.5 on 2022-08-22 18:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('libralian', '0006_alter_fines_actual_return_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fines',
            name='actual_return_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 18, 20, 23, 661863, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='fines',
            name='date_taken',
            field=models.DateField(default=datetime.datetime(2022, 8, 22, 18, 20, 23, 661863, tzinfo=utc), editable=False),
        ),
    ]
