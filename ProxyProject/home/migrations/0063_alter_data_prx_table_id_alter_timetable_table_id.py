# Generated by Django 4.1 on 2023-05-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0062_alter_data_prx_table_id_alter_sub_data_prx1_teacher_and_more'),
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
            field=models.CharField(max_length=2, unique=True),
        ),
    ]
