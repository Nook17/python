# Generated by Django 3.2.6 on 2021-08-26 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0002_auto_20210826_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
