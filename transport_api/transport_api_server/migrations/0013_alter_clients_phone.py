# Generated by Django 4.1.3 on 2022-12-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transport_api_server", "0012_alter_cars_license_alter_cars_payload_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clients",
            name="phone",
            field=models.CharField(max_length=11, unique=True),
        ),
    ]