# Generated by Django 4.0.2 on 2022-03-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acceso', '0004_alter_usuario_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=2, max_length=45, unique=True, verbose_name='Username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=200, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=45, unique=True, verbose_name='Nombre'),
        ),
    ]
