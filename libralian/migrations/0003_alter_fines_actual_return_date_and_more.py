# Generated by Django 4.0.5 on 2022-08-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libralian', '0002_remove_fines_extra_days_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fines',
            name='actual_return_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='fines',
            name='date_taken',
            field=models.DateField(auto_now_add=True),
        ),
    ]
