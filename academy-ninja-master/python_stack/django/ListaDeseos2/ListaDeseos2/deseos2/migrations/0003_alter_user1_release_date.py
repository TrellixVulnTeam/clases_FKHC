# Generated by Django 3.2.9 on 2021-12-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deseos2', '0002_alter_user1_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user1',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
