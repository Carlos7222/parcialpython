# Generated by Django 3.1.1 on 2022-09-21 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('edad', models.CharField(max_length=3)),
                ('peso', models.CharField(max_length=3)),
                ('frecuenciaCardiaca', models.CharField(max_length=3)),
                ('oxigenoSangre', models.CharField(max_length=3)),
                ('estres', models.CharField(max_length=3)),
            ],
        ),
    ]