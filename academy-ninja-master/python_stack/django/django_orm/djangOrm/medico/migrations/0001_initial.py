# Generated by Django 4.0.2 on 2022-03-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('especialidad', models.CharField(choices=[('A', 'Cardiologia'), ('B', 'Oftamologia'), ('C', 'Pediatria'), ('D', 'Otorrino'), ('E', 'Neurologia'), ('F', 'Urologia'), ('G', 'Medicina General')], default='G', max_length=1)),
                ('telefono', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
