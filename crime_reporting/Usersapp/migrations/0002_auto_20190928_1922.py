# Generated by Django 2.2.5 on 2019-09-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usersapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]