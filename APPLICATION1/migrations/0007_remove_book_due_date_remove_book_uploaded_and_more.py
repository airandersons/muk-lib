# Generated by Django 4.0.5 on 2022-08-02 07:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('APPLICATION1', '0006_remove_book_borrower_id_book_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Due_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Uploaded',
        ),
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 2, 7, 23, 20, 266273, tzinfo=utc), editable=False),
        ),
        migrations.AddField(
            model_name='book',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 2, 7, 23, 20, 266273, tzinfo=utc)),
        ),
    ]
