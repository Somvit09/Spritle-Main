# Generated by Django 4.1.5 on 2023-03-04 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0005_alter_timesheet_employee"),
    ]

    operations = [
        migrations.CreateModel(
            name="TaskModel",
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
                ("task", models.CharField(max_length=250)),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authentication.registerteacher",
                    ),
                ),
            ],
        ),
    ]
