# Generated by Django 3.2.9 on 2021-12-04 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deseos2', '0004_auto_20211204_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user1',
            name='first_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='user1',
            name='last_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='user1',
            name='password',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='user1',
            name='release_date',
            field=models.DateField(),
        ),
    ]
