# Generated by Django 5.0.6 on 2024-07-06 08:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="survey",
            name="have_breakfast",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="survey",
            name="is_exist_car",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="survey",
            name="len_of_reservation",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="survey",
            name="num_of_adult",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="survey",
            name="num_of_child",
            field=models.PositiveIntegerField(default=0),
        ),
    ]