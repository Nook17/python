# Generated by Django 2.2.10 on 2021-08-31 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfd', '0008_notesdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy_calc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sell_calc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_level', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='notesdb',
            name='amount_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notesdb',
            name='forex_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notesdb',
            name='gap',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notesdb',
            name='lot',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notesdb',
            name='margin_value',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notesdb',
            name='pip_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notesdb',
            name='tp_buy',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notesdb',
            name='tp_sell',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='notesdb',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='notesdb',
            name='percent_year',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
