# Generated by Django 4.2.11 on 2024-04-25 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_documentos_miniatura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentos',
            name='miniatura',
        ),
    ]
