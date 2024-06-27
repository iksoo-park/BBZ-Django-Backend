# Generated by Django 5.0.6 on 2024-06-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountLoginType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "loginType",
                    models.CharField(choices=[("KAKAO", "Kakao")], max_length=10),
                ),
            ],
            options={
                "db_table": "account_login_type",
            },
        ),
        migrations.AlterField(
            model_name="accountroletype",
            name="roleType",
            field=models.CharField(max_length=64),
        ),
    ]
