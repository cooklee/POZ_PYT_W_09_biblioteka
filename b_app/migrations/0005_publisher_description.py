# Generated by Django 4.0.2 on 2022-02-20 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b_app', '0004_publisher_city_publisher_street'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]