# Generated by Django 4.0.4 on 2022-06-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Address not available', max_length=80),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='Phone Not Provided', max_length=11),
        ),
    ]