# Generated by Django 4.0.6 on 2022-07-16 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPLICATION1', '0002_alter_book_bookcover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookcover',
            field=models.ImageField(upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='book',
            name='books',
            field=models.FileField(upload_to=''),
        ),
    ]
