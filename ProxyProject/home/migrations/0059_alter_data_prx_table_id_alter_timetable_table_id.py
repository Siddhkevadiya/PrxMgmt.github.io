# Generated by Django 4.1 on 2023-05-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0058_alter_data_prx_table_id_alter_timetable_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_prx',
            name='Table_Id',
            field=models.CharField(default=3, max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Table_Id',
            field=models.CharField(default=3, max_length=2, unique=True),
        ),
    ]
