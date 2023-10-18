# Generated by Django 4.1 on 2023-05-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_alter_data_prx_table_id_alter_timetable_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_prx',
            name='Table_Id',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Table_Id',
            field=models.CharField(default=22, max_length=2, unique=True),
        ),
    ]