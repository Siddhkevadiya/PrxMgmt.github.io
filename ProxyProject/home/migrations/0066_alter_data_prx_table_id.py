# Generated by Django 4.1 on 2023-05-25 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0065_alter_data_prx_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_prx',
            name='Table_Id',
            field=models.IntegerField(max_length=2, unique=True),
        ),
    ]
