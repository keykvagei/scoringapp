# Generated by Django 4.2.6 on 2023-10-26 09:21

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0002_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="total_rating_value",
            field=models.DecimalField(
                decimal_places=4, default=Decimal("0.00"), max_digits=100
            ),
        ),
    ]
