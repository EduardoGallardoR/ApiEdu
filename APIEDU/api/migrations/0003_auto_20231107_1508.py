# Generated by Django 3.2.4 on 2023-11-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_encuesta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='id_respuesta',
            field=models.AutoField(db_column='idrespuesta', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idUsuario',
            field=models.AutoField(db_column='idusu', primary_key=True, serialize=False),
        ),
    ]