# Generated by Django 4.1 on 2023-06-22 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0069_alter_data_prx_acronym_alter_data_prx_teacher_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='Acronym',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Teacher',
            field=models.CharField(max_length=50),
        ),
    ]