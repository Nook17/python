# Generated by Django 3.2.7 on 2021-09-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0023_auto_20210904_0809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pipmargin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market', models.CharField(max_length=255)),
                ('margin', models.IntegerField()),
                ('pip', models.FloatField()),
            ],
        ),
    ]
