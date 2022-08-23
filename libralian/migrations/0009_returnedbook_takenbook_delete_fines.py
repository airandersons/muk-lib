# Generated by Django 4.0.5 on 2022-08-22 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libralian', '0008_alter_fines_actual_return_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('book_title', models.TextField(max_length=20)),
                ('username', models.TextField(max_length=20)),
                ('category', models.TextField(max_length=20)),
                ('student_id', models.IntegerField()),
                ('date_taken', models.DateField(default=datetime.datetime(2022, 8, 22, 22, 14, 13, 718672))),
                ('return_date', models.DateField(default=datetime.datetime(2022, 8, 22, 22, 14, 13, 718672))),
                ('actual_return_date', models.DateField(default=datetime.datetime(2022, 8, 22, 22, 14, 13, 718672))),
            ],
        ),
        migrations.CreateModel(
            name='TakenBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.IntegerField()),
                ('book_title', models.TextField(max_length=20)),
                ('username', models.TextField(max_length=20)),
                ('category', models.TextField(max_length=20)),
                ('student_id', models.IntegerField()),
                ('date_taken', models.DateField(default=datetime.datetime(2022, 8, 22, 22, 14, 13, 638139))),
                ('return_date', models.DateField(default=datetime.datetime(2022, 8, 22, 22, 14, 13, 638139))),
            ],
        ),
        migrations.DeleteModel(
            name='Fines',
        ),
    ]