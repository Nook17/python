# Generated by Django 3.2.6 on 2021-08-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0005_auto_20210827_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposit',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='statement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
