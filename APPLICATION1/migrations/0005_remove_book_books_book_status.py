# Generated by Django 4.0.5 on 2022-08-02 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPLICATION1', '0004_alter_book_bookcover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='books',
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(default='Available', max_length=13),
        ),
    ]
