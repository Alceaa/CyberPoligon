# Generated by Django 5.1 on 2024-09-18 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyberpolygonApp', '0007_alter_role_role_name_alter_user_id_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cyberpolygonApp.role'),
        ),
    ]
