# Generated by Django 2.2 on 2022-10-27 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0010_auto_20221027_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='some string', upload_to='images/'),
        ),
    ]
