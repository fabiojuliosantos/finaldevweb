# Generated by Django 4.0.4 on 2022-07-19 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_alter_cursosdisponiveis_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursosdisponiveis',
            name='user',
        ),
    ]
