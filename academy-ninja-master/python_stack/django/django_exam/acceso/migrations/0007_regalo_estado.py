# Generated by Django 4.0.2 on 2022-03-05 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceso', '0006_regalo'),
    ]

    operations = [
        migrations.AddField(
            model_name='regalo',
            name='estado',
            field=models.TextField(default=0, max_length=1),
        ),
    ]
