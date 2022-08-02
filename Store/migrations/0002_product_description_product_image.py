# Generated by Django 4.0.4 on 2022-05-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='products\\download.jpg', upload_to='products\\download.jpg'),
        ),
    ]
