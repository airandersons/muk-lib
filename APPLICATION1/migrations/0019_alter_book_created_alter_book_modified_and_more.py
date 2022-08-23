# Generated by Django 4.0.5 on 2022-08-22 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPLICATION1', '0018_alter_book_created_alter_book_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookedbook',
            name='booking_end',
            field=models.DateTimeField(default=datetime.date(2022, 8, 26)),
        ),
        migrations.AlterField(
            model_name='bookedbook',
            name='booking_start',
            field=models.DateTimeField(default=datetime.date(2022, 8, 22)),
        ),
    ]
