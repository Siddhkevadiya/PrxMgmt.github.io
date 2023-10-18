# Generated by Django 4.1 on 2023-05-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0059_alter_data_prx_table_id_alter_timetable_table_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_prx',
            name='Table_Id',
            field=models.CharField(default=4, max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx10',
            name='EIGHTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx10',
            name='FIFTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx10',
            name='FIRST_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx10',
            name='FOURTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx10',
            name='NINETH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx10',
            name='SECOND_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx10',
            name='SEVENTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx10',
            name='SIXTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx10',
            name='THIRD_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx11',
            name='EIGHTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx11',
            name='FIFTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx11',
            name='FIRST_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx11',
            name='FOURTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx11',
            name='NINETH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx11',
            name='SECOND_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx11',
            name='SEVENTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx11',
            name='SIXTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx11',
            name='THIRD_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx2',
            name='EIGHTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx2',
            name='FIFTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx2',
            name='FIRST_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx2',
            name='FOURTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx2',
            name='NINETH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx2',
            name='SECOND_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx2',
            name='SEVENTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx2',
            name='SIXTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx2',
            name='THIRD_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx3',
            name='EIGHTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx3',
            name='FIFTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx3',
            name='FIRST_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx3',
            name='FOURTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx3',
            name='NINETH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx3',
            name='SECOND_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx3',
            name='SEVENTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx3',
            name='SIXTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx3',
            name='THIRD_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx4',
            name='EIGHTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx4',
            name='FIFTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx4',
            name='FIRST_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx4',
            name='FOURTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx4',
            name='NINETH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx4',
            name='SECOND_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx4',
            name='SEVENTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx4',
            name='SIXTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx4',
            name='THIRD_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx5',
            name='EIGHTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx5',
            name='FIFTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx5',
            name='FIRST_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx5',
            name='FOURTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx5',
            name='NINETH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx5',
            name='SECOND_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx5',
            name='SEVENTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx5',
            name='SIXTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx5',
            name='THIRD_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx6',
            name='EIGHTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx6',
            name='FIFTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx6',
            name='FIRST_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx6',
            name='FOURTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx6',
            name='NINETH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx6',
            name='SECOND_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx6',
            name='SEVENTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx6',
            name='SIXTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx6',
            name='THIRD_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx7',
            name='EIGHTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx7',
            name='FIFTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx7',
            name='FIRST_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx7',
            name='FOURTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx7',
            name='NINETH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx7',
            name='SECOND_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx7',
            name='SEVENTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx7',
            name='SIXTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx7',
            name='THIRD_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx8',
            name='EIGHTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx8',
            name='FIFTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx8',
            name='FIRST_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx8',
            name='FOURTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx8',
            name='NINETH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx8',
            name='SECOND_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx8',
            name='SEVENTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx8',
            name='SIXTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx8',
            name='THIRD_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx9',
            name='EIGHTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx9',
            name='FIFTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx9',
            name='FIRST_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx9',
            name='FOURTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx9',
            name='NINETH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx9',
            name='SECOND_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx9',
            name='SEVENTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx9',
            name='SIXTH_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='sub_data_prx9',
            name='THIRD_period',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Table_Id',
            field=models.CharField(default=46, max_length=2, unique=True),
        ),
    ]
