# Generated by Django 4.0.5 on 2022-07-16 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dz', '0002_authors_books_library_remove_book_author_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Library',
        ),
    ]
