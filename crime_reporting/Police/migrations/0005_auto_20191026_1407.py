# Generated by Django 2.2.5 on 2019-10-26 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Police', '0004_auto_20191026_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mostwanted',
            name='image',
            field=models.ImageField(upload_to='wanted_people'),
        ),
    ]