# Generated by Django 4.0.5 on 2022-08-22 13:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('book_title', models.TextField(max_length=20)),
                ('username', models.TextField(max_length=20)),
                ('category', models.TextField(max_length=20)),
                ('student_id', models.IntegerField()),
                ('date_taken', models.DateField(default=datetime.datetime(2022, 8, 22, 13, 44, 52, 31324, tzinfo=utc), editable=False)),
                ('actual_return_date', models.DateField(default=datetime.datetime(2022, 8, 22, 13, 44, 52, 31324, tzinfo=utc))),
                ('extra_days', models.IntegerField()),
                ('fine', models.IntegerField()),
            ],
        ),
    ]