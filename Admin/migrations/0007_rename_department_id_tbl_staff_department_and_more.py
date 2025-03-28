# Generated by Django 5.1.6 on 2025-02-19 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_staff'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_staff',
            old_name='department_id',
            new_name='department',
        ),
        migrations.AlterField(
            model_name='tbl_staff',
            name='staff_contact',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tbl_staff',
            name='staff_email',
            field=models.EmailField(max_length=50),
        ),
    ]
