# Generated by Django 5.1.6 on 2025-02-14 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_academic_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=50)),
                ('admin_contact', models.CharField(max_length=50)),
                ('admin_email', models.EmailField(max_length=50)),
                ('admin_password', models.CharField(max_length=50)),
            ],
        ),
    ]
