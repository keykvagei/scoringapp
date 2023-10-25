# Generated by Django 4.2.6 on 2023-10-25 13:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "profiles",
            "0003_profile_description_profile_name_alter_profile_rate_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="name",
        ),
        migrations.AddField(
            model_name="profile",
            name="role",
            field=models.CharField(
                choices=[
                    ("citizen", "Citizen"),
                    ("vip_citizen", "VIP Citizen"),
                    ("police", "Police"),
                    ("admin", "Admin"),
                ],
                default="citizen",
                max_length=12,
            ),
        ),
    ]
