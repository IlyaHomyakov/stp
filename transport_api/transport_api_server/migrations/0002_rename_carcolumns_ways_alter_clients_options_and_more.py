# Generated by Django 4.1.3 on 2022-11-19 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transport_api_server", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CarColumns",
            new_name="Ways",
        ),
        migrations.AlterModelOptions(
            name="clients",
            options={"verbose_name": "Clients", "verbose_name_plural": "Clients"},
        ),
        migrations.AlterModelOptions(
            name="orders",
            options={"verbose_name": "Orders", "verbose_name_plural": "Orders"},
        ),
        migrations.AlterModelOptions(
            name="ways",
            options={"verbose_name": "Ways", "verbose_name_plural": "Ways"},
        ),
    ]
