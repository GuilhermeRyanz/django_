# Generated by Django 5.1.1 on 2024-10-09 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_rename_active_client_dt_active_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='dt_active',
            new_name='cs_active',
        ),
    ]
