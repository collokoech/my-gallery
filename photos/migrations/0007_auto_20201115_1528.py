# Generated by Django 3.1.3 on 2020-11-15 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_auto_20201115_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
