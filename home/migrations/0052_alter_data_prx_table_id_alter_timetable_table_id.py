# Generated by Django 4.1 on 2023-05-20 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_delete_sub_data_prxs_remove_sub_timetable10_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_prx',
            name='Table_Id',
            field=models.CharField(default=9, max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Table_Id',
            field=models.CharField(default=12, max_length=2, unique=True),
        ),
    ]