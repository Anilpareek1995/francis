# Generated by Django 2.2.5 on 2019-10-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Police', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mostwanted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dob', models.IntegerField()),
                ('sex', models.CharField(max_length=20)),
                ('race', models.CharField(max_length=20)),
                ('hair', models.CharField(max_length=20)),
                ('eyes', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='missing_people')),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('charge', models.CharField(max_length=100)),
            ],
        ),
    ]
