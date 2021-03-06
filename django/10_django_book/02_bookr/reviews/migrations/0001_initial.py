# Generated by Django 4.0.5 on 2022-06-30 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Publish name', max_length=50)),
                ('website', models.URLField(help_text='web site address')),
                ('email', models.EmailField(help_text='email', max_length=254)),
            ],
        ),
    ]
