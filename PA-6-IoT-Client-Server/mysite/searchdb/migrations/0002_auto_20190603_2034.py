# Generated by Django 2.2.1 on 2019-06-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensorvalue',
            name='cds',
            field=models.IntegerField(default=0),
        ),
    ]