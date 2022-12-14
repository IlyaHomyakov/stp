# Generated by Django 4.1.3 on 2022-12-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transport_api_server", "0006_alter_orders_shipment_price_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="orders",
            name="mycustomconstraint_check1",
        ),
        migrations.AddConstraint(
            model_name="orders",
            constraint=models.CheckConstraint(
                check=models.Q(("recovery_date__gt", models.F("ship_date"))),
                name="ship_recovery_date_constraint",
            ),
        ),
    ]
