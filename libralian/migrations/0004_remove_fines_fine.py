# Generated by Django 4.0.5 on 2022-08-22 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libralian', '0003_alter_fines_actual_return_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fines',
            name='fine',
        ),
    ]
