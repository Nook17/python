# Generated by Django 3.2.6 on 2021-08-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0007_withdrawal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notesdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent_year', models.FloatField()),
            ],
        ),
    ]
