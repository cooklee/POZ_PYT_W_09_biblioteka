# Generated by Django 4.0.2 on 2022-02-20 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b_app', '0003_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='publisher',
            name='street',
            field=models.CharField(default='', max_length=40),
        ),
    ]