# Generated by Django 4.1.1 on 2022-11-13 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appCompeticion', '0010_detalle_grupo_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalle_grupo',
            name='slug',
        ),
    ]
