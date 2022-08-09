# Generated by Django 4.0.5 on 2022-08-02 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPLICATION1', '0005_remove_book_books_book_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='borrower_id',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
