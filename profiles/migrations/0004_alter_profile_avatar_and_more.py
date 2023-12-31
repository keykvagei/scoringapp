# Generated by Django 4.2.6 on 2023-10-27 22:00

from decimal import Decimal
from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0003_alter_profile_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                default="/static/images/default-user-image.png",
                upload_to=profiles.models.get_upload_to_avatar,
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="total_rating_value",
            field=models.DecimalField(
                decimal_places=4, default=Decimal("0.001"), max_digits=100
            ),
        ),
    ]
