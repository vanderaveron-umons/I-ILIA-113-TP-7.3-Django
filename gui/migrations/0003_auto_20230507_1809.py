# Generated by Django 3.2 on 2023-05-07 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui', '0002_auto_20230507_1808'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='client',
            table='client',
        ),
        migrations.AlterModelTable(
            name='commande',
            table='commande',
        ),
    ]
