# Generated by Django 4.2.11 on 2024-04-24 02:17

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentos',
            name='archivo',
            field=models.FileField(upload_to=catalog.models.change_file_name),
        ),
    ]
