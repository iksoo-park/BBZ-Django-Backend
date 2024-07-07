# Generated by Django 5.0.6 on 2024-07-05 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Survey",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("num_of_adult", models.PositiveIntegerField()),
                ("num_of_child", models.PositiveIntegerField()),
                ("have_breakfast", models.PositiveIntegerField()),
                ("is_exist_car", models.PositiveIntegerField()),
                ("len_of_reservation", models.PositiveIntegerField()),
                ("payment_date", models.DateTimeField(auto_now_add=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product",
                        to="product.product",
                    ),
                ),
            ],
            options={
                "db_table": "survey",
            },
        ),
    ]
