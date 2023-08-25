# Generated by Django 4.1.1 on 2022-11-14 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appEquipo', '0009_alineacion_remove_alineacion_equipo_encuentro_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alineacion',
            options={'verbose_name_plural': 'alineacion'},
        ),
        migrations.AddField(
            model_name='alineacion_equipo',
            name='alineacion_id',
            field=models.ForeignKey(db_column='alineacion_id', default=1, on_delete=django.db.models.deletion.CASCADE, to='appEquipo.alineacion'),
            preserve_default=False,
        ),
    ]