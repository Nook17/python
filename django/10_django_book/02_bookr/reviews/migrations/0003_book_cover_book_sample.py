# Generated by Django 4.0.6 on 2022-07-14 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_book_contributor_review_bookcontributor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='sample',
            field=models.FileField(blank=True, null=True, upload_to='book_samples/'),
        ),
    ]
